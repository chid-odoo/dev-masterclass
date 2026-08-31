from odoo import api, Command, fields, models

from odoo.exceptions import UserError, ValidationError

class LoanApplication(models.Model):
    _name = "loan.application"
    _description = "Loan Application"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    
    _name_uniq = models.Constraint(
        "UNIQUE(name)",
        "Two applications cannot share the same reference.",
    )
    _principal_check = models.Constraint(
        'CHECK(principal_amount > 0)', 
        'The principal amount must be strictly greater than zero.'
    )

    name = fields.Char(string="Application Number")

    loan_term = fields.Integer(string="Term (Months)", default=36)

    interest_rate = fields.Float(string="Interest Rate", required=True, digits=(5, 2))

    date_applied = fields.Date(
        string="Application Date", default=fields.Date.context_today
    )
    
    date_approved = fields.Date(string="Approval Date")

    date_rejected = fields.Date(string="Rejection Date")

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("sent", "Sent"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
        copy=False,
        tracking=True,
    )

    active = fields.Boolean(default=True)

    notes = fields.Html(string="Internal Notes", copy=False)

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Customer", required=True
    )

    email = fields.Char(related="partner_id.email")
    
    phone = fields.Char(related="partner_id.phone")

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
        default=lambda self: self.env.user,
    )

    product_id = fields.Many2one(comodel_name="product.product", string="Motorcycle")

    currency_id = fields.Many2one(
        comodel_name="res.currency", default=lambda self: self.env.company.currency_id
    )

    # The full price of the motorcycle, and the figure the user actually types.
    # required here rather than on loan_amount: once loan_amount is derived it is
    # not something anyone can be asked to fill in, and a required column with
    # nothing writing to it only produces NOT NULL errors.
    principal_amount = fields.Monetary(
        string="Principal Amount", required=True, currency_field="currency_id"
    )

    loan_amount = fields.Monetary(currency_field="currency_id", compute="_compute_loan_amount", inverse="_inverse_loan_amount")

    down_payment = fields.Monetary(currency_field="currency_id")

    tag_ids = fields.Many2many(comodel_name="loan.application.tag", string="Tags")

    document_ids = fields.One2many(
        comodel_name="loan.application.document",
        inverse_name="application_id",
        string="Compliance Documents",
    )

    # ---------------------------------------------------------
    # COMPUTE / INVERSE METHODS
    # ---------------------------------------------------------

    @api.depends("principal_amount", "down_payment")
    def _compute_loan_amount(self):
        for application in self:
            application.loan_amount = application.principal_amount - application.down_payment

    def _inverse_loan_amount(self):
        for application in self:
            application.down_payment = application.principal_amount - application.loan_amount

    # ---------------------------------------------------------
    # CONSTRAINTS
    # ---------------------------------------------------------

    @api.constrains("principal_amount", "down_payment")
    def _check_down_payment(self):
        for loan in self:
            if loan.down_payment >= loan.principal_amount:
                # We use self.env._() instead of the legacy global _() import
                raise ValidationError(
                    self.env._("The down payment cannot be greater than or equal to the principal amount.")
                )

    # ---------------------------------------------------------
    # ACTION METHODS
    # ---------------------------------------------------------

    # The three buttons in the form header call these methods by name. A method
    # behind a type="object" button takes no arguments beyond self, and whatever it
    # returns goes back to the web client — returning nothing simply reloads the
    # record, which is all a transition needs to do.
    #
    # action_approve_loan below is written out as the worked example. The other two
    # follow its shape: loop over self, skip any record that is not in the state the
    # transition starts from, then write the change.

    def action_approve_loan(self):
        """Worked example: the approval transition, start to finish."""
        for loan in self:
            if loan.state != "sent":
                continue
            # Both values in one write, deliberately. Each assignment would be a
            # write of its own with its own access check, and the Day 1 record rule
            # only lets group_kawiil_financing_user write to applications that are
            # not yet approved — so a second write arriving once the state is already
            # "approved" is refused for those users. Testing as an admin hides it:
            # rules from different groups are OR'd, and the admin rule lets it pass.
            loan.write(
                {
                    "state": "approved",
                    "date_approved": fields.Date.context_today(loan),
                }
            )

    def action_reject_loan(self):
        for loan in self:
            if loan.state != "sent":
                continue
            loan.write(
                {
                    "state": "rejected",
                    "date_rejected": fields.Date.context_today(loan),
                }
            )

    def action_submit(self):
        for loan in self:
            if loan.state != "draft":
                continue
            required_docs = loan.document_ids.filtered(
                lambda doc: doc._is_required_for_submit()
            )
            if not required_docs:
                raise UserError(
                    self.env._(
                        "Attach the required supporting documents before submitting"
                    )
                )
            unapproved = required_docs.filtered(
                lambda doc: not doc._is_valid_for_submit()
            )
            if unapproved:
                raise UserError(
                    self.env._("Every required document must be approved before the "
                    "application is submitted. '%s' is not.",
                    unapproved[0].type_id.display_name,)
            )
            loan.write(
                {
                    "state": "sent",
                    "date_applied": fields.Date.context_today(loan),
                }
            )

            loan.message_post(
                body=self.env._("Application successfully submitted for review!"),
                subtype_xmlid="mail.mt_note",
            )

    # ---------------------------------------------------------
    # CRUD OVERRIDES
    # ---------------------------------------------------------

    @api.model
    def _get_default_document_types(self):
        """The document types that belong on a new application's checklist."""
        # search([]) already leaves out the archived types: the model has an `active`
        # field, and Odoo filters on it unless you tell it otherwise.
        return self.env["loan.application.document.type"].search([])

    @api.model_create_multi
    def create(self, vals_list):
        """
        Overrides standard creation to automatically inject the 
        required document checklist.
        """
        # 1. Fetch the default types using our extensible helper
        doc_types = self._get_default_document_types()

        # 2. Modify the incoming dictionaries before they hit the database
        for vals in vals_list:
            if doc_types:
                # Prepare the creation commands
                commands = [Command.create({'type_id': dt.id}) for dt in doc_types]
                
                # Append to existing document_ids if they exist, otherwise initialize
                vals['document_ids'] = vals.get('document_ids', []) + commands

        # 3. Pass the modified vals_list to the standard ORM creation method
        return super().create(vals_list)
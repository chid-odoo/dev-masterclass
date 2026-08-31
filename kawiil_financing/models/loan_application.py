# TODO (3.01): the compute method you write below is decorated with
# @api.depends, so `api` has to join this import.
from odoo import fields, models

# TODO (3.02): raising a ValidationError means importing it first:
#     from odoo.exceptions import ValidationError

# TODO (3.03): UserError comes from the same module, so one import line covers
# both: from odoo.exceptions import UserError, ValidationError

# TODO (3.04): Command joins the odoo import. Mind the order ruff wants —
# capitals sort first: from odoo import Command, api, fields, models


class LoanApplication(models.Model):
    _name = "loan.application"
    _description = "Loan Application"

    # TODO (3.06): mix the chatter into this model by adding _inherit alongside the
    # two lines above — keep _name, do not replace it:
    #
    #     _inherit = ["mail.thread", "mail.activity.mixin"]
    #
    # mail.thread brings the message history and followers; mail.activity.mixin
    # brings scheduled activities. Both are AbstractModels: they have no table of
    # their own, so nothing is copied at the database level, their fields and methods
    # are simply folded into this model. That is why they are called mixins, though
    # the mechanism is the same _name-plus-_inherit pairing you will use for real
    # prototype inheritance in the final task.
    #
    # The mail module is already in the dependency graph, through product, so the
    # manifest needs no change. Worth knowing that a module normally declares what it
    # uses directly rather than leaning on someone else's dependency — this one is
    # a deliberate shortcut, not the habit to take home.

    # Database-level constraints, written with the models.Constraint API that
    # replaced _sql_constraints in Odoo 19: a class attribute holding the SQL and
    # the message shown when it is violated. Postgres enforces them, so they hold
    # however the record was made — the form, an import, or the shell — which is
    # exactly what makes them worth having.
    _name_uniq = models.Constraint(
        "UNIQUE(name)",
        "Two applications cannot share the same reference.",
    )

    # TODO (3.02): a second one, following the example above: a CHECK that keeps
    # principal_amount strictly above zero. Nobody finances a motorcycle that costs
    # nothing, and a principal of zero would make the loan arithmetic meaningless.

    name = fields.Char(string="Application Number")

    loan_term = fields.Integer(string="Term (Months)", default=36)

    interest_rate = fields.Float(string="Interest Rate", required=True, digits=(5, 2))

    date_applied = fields.Date(
        string="Application Date", default=fields.Date.context_today
    )

    # No default on these two: they are stamped by the action methods when the
    # decision is actually taken, not when the record is created.
    date_approved = fields.Date(string="Approval Date")

    date_rejected = fields.Date(string="Rejection Date")

    # TODO (3.06): once the chatter is in place, add tracking=True to this field and
    # to principal_amount. Every change to a tracked field is then written into the
    # record's message history by itself, with the old and new values side by side.
    #
    # Only these two. Tracking every field turns the chatter into noise nobody reads,
    # which is worse than not having it: pick the ones somebody would be asked to
    # account for later.
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("sent", "Sent"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="draft",
        copy=False,
    )

    active = fields.Boolean(default=True)

    notes = fields.Html(string="Internal Notes", copy=False)

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Customer", required=True
    )

    # TODO (3.01): add two related fields that pull the customer's contact details
    # onto this form: `email` from the partner's email, `phone` from the partner's
    # phone. Both are Char. A related field is a computed field underneath, so
    # leave the defaults alone — read-only, and not stored in the database.

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

    # TODO (3.01): loan_amount stops being a figure anyone types in.
    #   - compute it from principal_amount - down_payment, in a method that
    #     iterates explicitly with `for record in self:`
    #   - decorate that method with @api.depends on both source fields
    #   - give the field an inverse method as well, so that typing a loan_amount
    #     works the deposit back out: down_payment = principal_amount - loan_amount
    # Two things to expect once it is computed: a computed field is read-only
    # unless it declares an inverse, and an unstored one cannot be searched or
    # sorted, so COMMANDS.md's search([("loan_amount", ">", 10000)]) snippet stops
    # working and the list view column stops sorting. store=True, or a search=
    # method, brings those back.
    loan_amount = fields.Monetary(currency_field="currency_id")

    down_payment = fields.Monetary(currency_field="currency_id")

   
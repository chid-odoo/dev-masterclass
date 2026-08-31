from odoo import fields, models


class LoanApplicationDocument(models.Model):
    _name = "loan.application.document"
    _description = "Loan Application Document"

    name = fields.Char(string="Reference/Notes")
    state = fields.Selection(
        [("new", "New"), ("approved", "Approved"), ("rejected", "Rejected")],
        string="Status",
        default="new",
        required=True,
    )

    # Links to the configuration table
    type_id = fields.Many2one(
        comodel_name="loan.application.document.type",
        string="Document Type",
        required=True,
    )

    # The crucial foreign key that links this line back to the parent Loan
    application_id = fields.Many2one(
        comodel_name="loan.application",
        string="Application",
        ondelete="cascade",  # If the loan is deleted, delete these lines too
    )

    # Links to Odoo's native attachment model to handle actual file uploads
    attachment_id = fields.Many2one(comodel_name="ir.attachment", string="File")

    # ---------------------------------------------------------
    # ACTION METHODS
    # ---------------------------------------------------------

    # One action method per button in the inline checklist. A button with
    # type="object" calls the method on the record it is sitting on, so `self` here
    # is the single document line whose button was clicked.

    def action_approve_document(self):
        self.state = "approved"

    # TODO (3.03): the other half of the pair. Same shape as the method above, with
    # the state it belongs to. The button you add for it is wired by this name.

    def action_reject_document(self):
        # TODO (3.03): set state to "rejected".
        pass

    # ---------------------------------------------------------
    # SUBMISSION RULES
    # ---------------------------------------------------------

    # The loan application asks each of its lines these two questions when someone
    # tries to submit it. They live here, on the document, rather than in the
    # application: the application never has to know how a document makes up its
    # mind, and when the rules change they change in one place. You will call both
    # from action_submit at 3.03.
    #
    # Both are called on one line at a time, so `self` is a single record here.

    def _is_required_for_submit(self):
        """Whether this line must be settled before its application can go out."""
        return self.type_id.is_required

    def _is_valid_for_submit(self):
        """Whether this line is in a state the application can be submitted with."""
        return self.state == "approved"

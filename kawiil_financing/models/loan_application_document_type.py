from odoo import fields, models


class LoanApplicationDocumentType(models.Model):
    _name = "loan.application.document.type"
    _description = "Loan Application Document Type"

    name = fields.Char(string="Document Name", required=True)
    is_required = fields.Boolean(string="Required", default=False)
    # Standard Odoo soft-delete flag
    active = fields.Boolean(string="Active", default=True)

from odoo import fields, models


class LoanApplicationTag(models.Model):
    _name = "loan.application.tag"
    _description = "Loan Application Tag"

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color")

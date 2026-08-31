# ODOP assignment 2.08 - tags.
#
# This whole file is a worked example. It is the smallest complete model you
# will write, so read it as the pattern for the two next to it.

from odoo import fields, models


class LoanApplicationTag(models.Model):
    _name = "loan.application.tag"
    _description = "Loan Application Tag"

    name = fields.Char(string="Tag Name", required=True)
    # An Integer, not a colour code. Odoo's colour picker works off an index
    # from 0 to 11 that maps onto a fixed palette in the web client, so every
    # app ends up using the same colours.
    color = fields.Integer(string="Color")

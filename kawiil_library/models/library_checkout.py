from odoo import api, fields, models


class LibraryCheckout(models.Model):
    _name = "library.checkout"
    _description = "Library Checkout"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "checkout_date desc"

    name = fields.Char(
        string="Reference",
        required=True,
        copy=False,
        readonly=True,
        default="New",
    )
    book_id = fields.Many2one(
        comodel_name="library.book",
        string="Book",
        required=True,
        tracking=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        required=True,
        tracking=True,
    )
    checkout_date = fields.Date(
        string="Checkout Date",
        default=fields.Date.today,
        required=True,
        tracking=True,
    )
    due_date = fields.Date(string="Due Date", tracking=True)
    return_date = fields.Date(string="Return Date", tracking=True)
    state = fields.Selection(
        selection=[
            ("ongoing", "Checked Out"),
            ("returned", "Returned"),
            ("overdue", "Overdue"),
        ],
        string="Status",
        default="ongoing",
        tracking=True,
    )
    notes = fields.Text(string="Notes")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "New") == "New":
                vals["name"] = self.env["ir.sequence"].next_by_code("library.checkout") or "New"
        return super().create(vals_list)

    def action_return(self):
        self.write({
            "state": "returned",
            "return_date": fields.Date.today(),
        })

    def action_mark_overdue(self):
        self.write({"state": "overdue"})

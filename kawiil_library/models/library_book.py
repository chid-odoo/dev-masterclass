from odoo import api, fields, models


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "title"

    title = fields.Char(string="Title", required=True, tracking=True)
    author = fields.Char(string="Author", tracking=True)
    isbn = fields.Char(string="ISBN")
    state = fields.Selection(
        selection=[
            ("available", "Available"),
            ("checked_out", "Checked Out"),
        ],
        string="Status",
        default="available",
        tracking=True,
        compute="_compute_state",
        store=True,
    )
    checkout_ids = fields.One2many(
        comodel_name="library.checkout",
        inverse_name="book_id",
        string="Checkout History",
    )
    active_checkout_id = fields.Many2one(
        comodel_name="library.checkout",
        string="Checked Out By",
        compute="_compute_active_checkout",
        store=True,
    )
    checkout_count = fields.Integer(
        string="Total Checkouts",
        compute="_compute_checkout_count",
    )

    @api.depends("checkout_ids", "checkout_ids.state")
    def _compute_state(self):
        for book in self:
            ongoing = book.checkout_ids.filtered(lambda c: c.state == "ongoing")
            book.state = "checked_out" if ongoing else "available"

    @api.depends("checkout_ids", "checkout_ids.state")
    def _compute_active_checkout(self):
        for book in self:
            ongoing = book.checkout_ids.filtered(lambda c: c.state == "ongoing")
            book.active_checkout_id = ongoing[:1]

    def _compute_checkout_count(self):
        for book in self:
            book.checkout_count = len(book.checkout_ids)

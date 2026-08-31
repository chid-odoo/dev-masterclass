# ODOP assignments 2.02, 2.03, 2.07 and 2.08 — the loan.application model.
#
# Fill in every field marked TODO, working through the sections in order. Each
# section starts with one field written out as a worked example — copy its
# shape for the rest.
#
# Two things to get right once the fields are done, or none of this will load:
#   models/__init__.py            must import this file.
#   kawiil_financing/__init__.py  must import the models folder.

from odoo import fields, models


class LoanApplication(models.Model):
    # The technical name of the model. Odoo derives the database table from it
    # by swapping dots for underscores, so this becomes loan_application. You
    # will use this string everywhere: in XML, in the ORM, and in the Models
    # list under Settings > Technical.
    _name = "loan.application"
    # A human-readable label. Odoo uses it in error messages and in the Models
    # list. Always set it — Odoo logs a warning if you don't.
    _description = "Loan Application"

    # --- Assignment 2.02: the application's own data -----------------------

    # Worked example. "string" is the label the user sees on screen. Leave it
    # off and Odoo derives one from the field name, which would give you "Name"
    # here rather than "Application Number".
    name = fields.Char(string="Application Number")

    # TODO: loan_term — Integer, labelled "Term (Months)", defaulting to 36.

    # TODO: interest_rate — Float, labelled "Interest Rate", required=True.
    #       Pass digits=(5, 2) to store 5 digits in total with 2 of them after
    #       the decimal point.

    # TODO: date_applied — Date, labelled "Application Date", defaulting to
    #       today: default=fields.Date.context_today
    #
    #       Note there are no brackets and no lambda. A default takes the
    #       function itself and Odoo calls it per record. Use context_today
    #       rather than today: today gives the server's date, context_today
    #       gives the date in the user's own timezone, which is what someone
    #       filing an application late in the evening expects to see.

    # TODO: state — Selection offering, in this order: Draft, Sent, Approved,
    #       Rejected. The value is a list of (technical_key, label) tuples —
    #       the key is what gets stored, the label is what the user reads. Use
    #       the keys draft, sent, approved and rejected, and default to
    #       "draft". There is no cancelled state: abandoning an application
    #       means archiving it with the active field below.
    #
    #       Also pass copy=False. Duplicating an approved loan should give
    #       you a fresh draft to work from, not a second loan that claims to
    #       be approved. copy=False makes Odoo fall back to the default
    #       instead of carrying the value over.

    # TODO: active — Boolean defaulting to True. Odoo treats this exact field
    #       name specially: setting it to False hides the record from list
    #       views instead of deleting it, which is how archiving works.

    # TODO: notes — Html, labelled "Internal Notes", copy=False. Notes are
    #       about one specific application, so they should not follow a
    #       duplicate to the new record.

    # --- Assignment 2.03: links to the rest of Odoo ------------------------

    # Worked example. Uncomment it when you reach 2.03. A Many2one holds a
    # link to one record in another model. comodel_name says which model, and
    # Odoo stores the other record's database id in a partner_id column.
    # partner_id = fields.Many2one(
    #     comodel_name="res.partner", string="Customer", required=True
    # )

    # TODO: user_id — Many2one to "res.users", labelled "Salesperson",
    #       defaulting to whoever is logged in. self.env.user is the current
    #       user, so: default=lambda self: self.env.user

    # TODO: product_id — Many2one to "product.product", labelled "Motorcycle".
    #       product.product is the variant, the record that actually gets sold
    #       and stocked. product.template is the abstract product above it.

    # TODO: currency_id — Many2one to "res.currency". A Monetary field cannot
    #       format an amount without knowing its currency, so give this one a
    #       default rather than leaving it empty:
    #       default=lambda self: self.env.company.currency_id

    # TODO: loan_amount — Monetary, required=True, with
    #       currency_field="currency_id".

    # TODO: down_payment — Monetary, with currency_field="currency_id".
    #
    #       Monetary is a Float that Odoo renders with a currency symbol and
    #       the right number of decimals. The field named in currency_field
    #       has to exist on this same model, which is why currency_id comes
    #       first.

    # --- Assignment 2.08: categorisation and compliance --------------------

    # Worked example. Uncomment it when you reach 2.08, once the tag model
    # next door exists. A Many2many links this record to many tags, and each
    # tag back to many loans. Odoo quietly creates the join table that makes
    # that work; you never touch it.
    # tag_ids = fields.Many2many(comodel_name="loan.application.tag", string="Tags")

    # TODO: document_ids — One2many to "loan.application.document", labelled
    #       "Documents". A One2many is not stored: it is the mirror image of a
    #       Many2one on the other model, so it has to be told which field over
    #       there points back here. That is the second argument,
    #       inverse_name="application_id".

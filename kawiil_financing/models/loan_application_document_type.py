# ODOP assignment 2.08 - document types.
#
# The kinds of paperwork a loan can require: proof of identity, proof of
# income, and so on. Configuration data, edited by admins and referenced by
# the documents themselves.
#
# Follow the pattern in loan_application_tag.py.

# fields is unused until you write your first field below, which makes the
# Quality Gate flag it as an unused import. noqa silences that one check on
# this one line. Delete the comment once you have added a field.
from odoo import fields, models  # noqa: F401


class LoanApplicationDocumentType(models.Model):
    _name = "loan.application.document.type"
    _description = "Loan Application Document Type"

    # TODO: name — Char. Every model wants a name field: it is what Odoo shows
    #       when this record appears in a dropdown somewhere else.

    # TODO: is_required — Boolean. Whether a loan cannot proceed without this
    #       kind of document.

    # TODO: active — Boolean, default True. The archiving field again, same as
    #       on loan.application. A retired document type gets archived rather
    #       than deleted, so the old records still pointing at it keep working.

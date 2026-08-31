# ODOP assignment 2.08 - documents.
#
# One piece of paperwork attached to one loan application. This is the model
# behind the Compliance Checklist tab you will add to the loan form.
#
# Follow the pattern in loan_application_tag.py.

# fields is unused until you write your first field below, which makes the
# Quality Gate flag it as an unused import. noqa silences that one check on
# this one line. Delete the comment once you have added a field.
from odoo import fields, models  # noqa: F401


class LoanApplicationDocument(models.Model):
    _name = "loan.application.document"
    _description = "Loan Application Document"

    # TODO: name — Char, the document's label.

    # TODO: state — Selection with keys new, approved and rejected, labelled
    #       New, Approved and Rejected. Default to "new".

    # TODO: type_id — Many2one to "loan.application.document.type", labelled
    #       "Document Type".

    # TODO: application_id — Many2one to "loan.application", labelled
    #       "Loan Application". This is the field that document_ids on the
    #       loan points back through, so the two have to agree: name it
    #       exactly this or the One2many will not resolve.

    # TODO: attachment_id — Many2one to "ir.attachment", labelled "File".
    #       ir.attachment is Odoo's own model for stored files, so you get
    #       upload and download for free instead of building it.

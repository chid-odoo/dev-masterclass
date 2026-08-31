# TODO: import each model file so Odoo loads it.
#
# Odoo uses one relative import per file, with no .py extension:
#     from . import <file_name>
#
# By assignment 2.08 there are four:
#     loan_application            the main model            (2.02)
#     loan_application_tag        tags                      (2.08)
#     loan_application_document_type                        (2.08)
#     loan_application_document                             (2.08)
#
# Nothing in this folder is loaded until it is imported here, and this file in
# turn does nothing until kawiil_financing/__init__.py imports the folder.

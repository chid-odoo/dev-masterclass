# TODO (3.07): switch the tests on by importing the module beside this one:
#     from . import test_loan_application
#
# The tests themselves are already written — read them, then run them. This one line
# is what makes Odoo see them.
#
# Odoo finds the tests/ package on its own, and it must not be imported from the
# module's main __init__.py, or the test code would load in every database that
# installs this module rather than only the ones running tests. A test module missing
# from this file simply never runs: the suite reports success having executed
# nothing, which is the most expensive kind of green.

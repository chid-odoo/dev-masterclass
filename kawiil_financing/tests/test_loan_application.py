from odoo.exceptions import UserError, ValidationError
from odoo.tests import TransactionCase


class TestLoanApplication(TransactionCase):
    """Tests for the loan application's computes, constraints and workflow.

    Each one covers something built earlier in the day: the arithmetic from 3.01,
    the constraint from 3.02, the submission guard from 3.03 and the create
    override from 3.04. Break any of those and the matching test here says so.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # setUpClass runs once for the whole class, and everything it touches is
        # rolled back when the class finishes. Records made here are shared by every
        # test below and cost one round of database work; the same code in setUp
        # would run again before each test. That is the whole reason to prefer it.
        cls.partner = cls.env["res.partner"].create({"name": "Test Rider"})
        cls.document_type = cls.env["loan.application.document.type"].create(
            {
                "name": "Test Proof of Identity",
                "is_required": True,
            }
        )

    def _create_loan(self, **values):
        """A valid application, with anything passed in overriding the defaults.

        `name` is deliberately left unset. The unique constraint from 3.02 would
        collide if every test used the same reference, and Postgres is content with
        repeated NULLs.
        """
        return self.env["loan.application"].create(
            {
                "partner_id": self.partner.id,
                "principal_amount": 10000.0,
                "down_payment": 2000.0,
                "interest_rate": 7.5,
                **values,
            }
        )

    def test_01_computes_and_crud(self):
        """The loan amount is derived, and the checklist builds itself."""
        loan = self._create_loan()
        self.assertEqual(
            loan.loan_amount,
            8000.0,
            "loan_amount should be the principal less the down payment",
        )
        self.assertTrue(
            loan.document_ids,
            "create() should have built a checklist from the document types",
        )

    def test_02_python_constraints(self):
        """A deposit larger than the motorcycle is refused."""
        # Wrapping create() is enough: Odoo validates @api.constrains as part of
        # creating the record, so the error is raised before create() returns and
        # nothing needs flushing by hand.
        with self.assertRaises(ValidationError):
            self._create_loan(principal_amount=5000.0, down_payment=10000.0)

    def test_03_workflow_user_error(self):
        """An application whose checklist is unsettled cannot be submitted."""
        loan = self._create_loan()
        self.assertEqual(loan.state, "draft")
        # The lines create() added are still "new". Note which exception this is:
        # the constraint above raises ValidationError because it is a rule about the
        # data, while this one raises UserError because it is a rule about what
        # somebody is allowed to do next.
        with self.assertRaises(UserError):
            loan.action_submit()

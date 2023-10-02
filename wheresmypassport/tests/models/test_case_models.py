from wheresmypassport.models.Case.Case import CaseModel
from wheresmypassport.models.User.User import UserModel
from wheresmypassport.enums import CaseStatus

import unittest
import datetime
import uuid


class CaseModelTest(unittest.TestCase):

    def setUp(self):
        """Set up a test case"""
        self.user = UserModel("John123", "somepassword", "John")
        self.test_case = CaseModel(
            requested=datetime.datetime.now(),
            received=None,
            current_status=CaseStatus.,
            old_passport=uuid.uuid4(),
            new_passport=uuid.uuid4(),
            user=self.user,
            user_id=self.user.id
        )

    def test_requested_datetime(self):
        """Test if 'requested' datetime is set correctly"""
        self.assertIsInstance(self.test_case.requested, datetime.datetime)

    def test_received_datetime(self):
        """Test if 'received' datetime is None"""
        self.assertIsNone(self.test_case.received)

    def test_current_status(self):
        """Test if 'current_status' is set correctly"""
        self.assertEqual(self.test_case.current_status, 'initial request')

    def test_old_passport(self):
        """Test if 'old_passport' is set correctly"""
        self.assertIsInstance(self.test_case.old_passport, uuid.UUID)

    def test_new_passport(self):
        """Test if 'new_passport' is set correctly"""
        self.assertIsInstance(self.test_case.new_passport, uuid.UUID)

    def test_user(self):
        """Test if user is set correctly"""
        self.assertEqual(self.test_case.user, self.user)

    def test_user_id(self):
        """Test if 'user_id' is set correctly"""
        self.assertEqual(self.test_case.user_id, self.user.id)

    def test_change_status(self):
        """Test changing the case status"""
        self.test_case.current_status = "documents sent"
        self.assertEqual(self.test_case.current_status)

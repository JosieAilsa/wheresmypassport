from wheresmypassport.models.User.User import UserModel

import unittest


class UserModelTest(unittest.TestCase):

    def setUp(self):
        """Set up a test user"""
        self.test_user = UserModel("John123", "somepassword", "John")
                
    def test_username(self):
        """Test if username is set correctly"""
        self.assertEqual(self.test_user.username, "John123")

    def test_password(self):
        """Test if password is set correctly"""
        self.assertTrue(self.test_user.get_password("somepassword"))  # This is a simple example. Ideally, passwords should be hashed.

    def test_name(self):
        """Test if name is set correctly"""
        self.assertEqual(self.test_user.name, "John")

    def test_change_username(self):
        """Test changing the username"""
        self.test_user.username = "John124"
        self.assertEqual(self.test_user.username, "John124")


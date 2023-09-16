import unittest

from ...wheresmypassport.repositories.UserRepository import UserRepository


class TestUserRepo(unittest.TestCase):

    @patch('your_project.user_repo.some_dependency')  # Mock dependencies
    def setUp(self, mock_dependency):
        self.mock_dependency = mock_dependency
        self.user_repo = UserRepository()

    def test_create_user(self):
        user_data = {
            'username': 'SomeUser', 
            'password': 'Password123', 
            'name': 'Jon Snow', 
            

        }
        
        result = self.user_repo.create_user(user_data)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertIn('id', result)
        self.assertEqual(result['username'], 'john_doe')
        self.assertEqual(result['email'], 'john@example.com')

    def test_get_user_by_id(self):
        # Arrange
        user_id = 'some_id'

        # Act
        result = self.user_repo.get_user_by_id(user_id)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['id'], user_id)

    def test_update_user(self):
        # Arrange
        user_id = 'some_id'
        new_data = {'email': 'new_email@example.com'}

        # Act
        result = self.user_repo.update_user(user_id, new_data)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result['email'], new_data['email'])

    def test_delete_user(self):
        # Arrange
        user_id = 'some_id'

        # Act
        self.user_repo.delete_user(user_id)

        # Assert
        result = self.user_repo.get_user_by_id(user_id)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

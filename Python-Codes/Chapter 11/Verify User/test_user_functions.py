import unittest
from user_functions import verify_user

class VerifyUserTestCase(unittest.TestCase):
    """Tests for verify_user()."""

    def setUp(self):
        """Set up a list of active users to test against."""
        self.active_users = ['alice', 'bob', 'charlie']

    def test_user_found_exact_case(self):
        """verify_user returns True if username is in list (exact case)."""
        result = verify_user('alice', self.active_users)
        self.assertTrue(result)

    def test_user_found_different_case(self):
        """verify_user returns True if username matches ignoring case."""
        result = verify_user('Alice', self.active_users)
        self.assertTrue(result)

    def test_user_not_found(self):
        """verify_user returns False if username isn’t in list."""
        result = verify_user('david', self.active_users)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

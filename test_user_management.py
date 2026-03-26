import unittest
from user_management import set_db, create_user, get_user, \
    list_users, delete_user
from db_mock import MockDB

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.mock_db = MockDB()
        set_db(self.mock_db)

    def test_create_user_success(self):
        data = create_user("Example", "example@domain.com", \
                           "StrongP@ssw0rd", "1990-01-01")
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "Example")

    def test_create_user_invalid_name(self):
        with self.assertRaises(ValueError):
            create_user("Alex", "alex@domain.com", \
                        "StrongP@ssw0rd", "1990-01-01")

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            create_user("Example", "invalid-email", \
                        "StrongP@ssw0rd", "1990-01-01")

    def test_create_user_invalid_dob(self):
        with self.assertRaises(ValueError):
            create_user("Example", "example@domain.com", \
                        "StrongP@ssw0rd", "31-12-1990")

    def test_create_user_weak_password(self):
        with self.assertRaises(ValueError):
            create_user("Example", "example@domain.com", \
                        "weak", "1990-01-01")

    def test_get_list_delete(self):
        user = create_user("Example", "example@domain.com", \
                           "StrongP@ssw0rd", "1990-01-01")
        self.assertEqual(get_user(user["id"])["email"], "example@domain.com")
        self.assertEqual(len(list_users()), 1)
        self.assertTrue(delete_user(user["id"]))
        self.assertIsNone(get_user(user["id"]))


if __name__ == "__main__":
    unittest.main()

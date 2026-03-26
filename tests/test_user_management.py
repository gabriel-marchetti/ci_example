import unittest
from app.user_management import set_db, create_user, get_user, \
    list_users, delete_user
from app.db.db_mock import MockDB


class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.mock_db = MockDB()
        set_db(self.mock_db)

    def test_create_user_success(self):
        data = create_user("Example", "example@domain.com",
                           "StrongP@ssw0rd", "1990-01-01")
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "Example")

    def test_create_user_invalid_name(self):
        with self.assertRaises(ValueError):
            create_user("Alex", "alex@domain.com",
                        "StrongP@ssw0rd", "1990-01-01")

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            create_user("Example", "invalid-email",
                        "StrongP@ssw0rd", "1990-01-01")

    def test_create_user_invalid_dob(self):
        with self.assertRaises(ValueError):
            create_user("Example", "example@domain.com",
                        "StrongP@ssw0rd", "31-12-1990")

    def test_create_user_weak_password(self):
        with self.assertRaises(ValueError):
            create_user("Example", "example@domain.com",
                        "weak", "1990-01-01")

    def test_get_user_after_create(self):
        user = create_user("Example", "example@domain.com",
                           "StrongP@ssw0rd", "1990-01-01")
        self.assertEqual(get_user(user["id"])["email"], "example@domain.com")

    def test_list_users_after_create(self):
        create_user("Example", "example@domain.com",
                    "StrongP@ssw0rd", "1990-01-01")
        self.assertEqual(len(list_users()), 1)

    def test_delete_user(self):
        user = create_user("Example", "example@domain.com",
                           "StrongP@ssw0rd", "1990-01-01")
        self.assertTrue(delete_user(user["id"]))
        self.assertIsNone(get_user(user["id"]))

    def test_list_users_sorted_by_email(self):
        create_user(
            'User C',
            'charlie@domain.com',
            'StrongP@ssw0rd',
            '1990-01-01'
        )
        create_user(
            'User A',
            'alice@domain.com',
            'StrongP@ssw0rd',
            '1990-01-01'
        )
        create_user(
            'User B',
            'bob@domain.com',
            'StrongP@ssw0rd',
            '1990-01-01'
        )

        users = list_users()
        emails = [u["email"] for u in users]

        self.assertEqual(
            emails,
            sorted(emails),
            "list_users should return users sorted by email."
        )


if __name__ == "__main__":
    unittest.main()

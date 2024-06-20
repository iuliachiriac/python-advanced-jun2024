import json
import os
import unittest

from process_users import get_users, get_name_age


class TestGetUsers(unittest.TestCase):
    valid_file = "file.json"
    users = [
        {"name": "Anna", "age": 20},
        {"name": "John", "age": 40},
    ]

    @classmethod
    def setUpClass(cls):
        with open(cls.valid_file, "w") as f:
            json.dump(cls.users, f)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.valid_file)

    def test_nonexistent_file(self):
        output = get_users("nonexistent.txt")
        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 0)

    def test_file_does_not_contain_json(self):
        with open("file.txt", "w") as f:
            f.write("test")

        with self.assertRaises(json.JSONDecodeError):
            get_users("file.txt")

        os.remove("file.txt")

    def test_valid_file(self):
        output = get_users(self.valid_file)

        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 2)
        self.assertEqual(output, self.users)

    def test_valid_file_filter_age(self):
        output = get_users(self.valid_file, 15, age_max=25)

        self.assertIsInstance(output, list)
        self.assertEqual(len(output), 1)
        self.assertEqual(output, [{"name": "Anna", "age": 20}])


class TestGetNameAge(unittest.TestCase):
    def test_valid_user(self):
        users = [
            {"name": "Anna", "age": 20},
            {"name": "John", "age": 40},
        ]
        for user in users:
            with self.subTest(user=user):
                output = get_name_age(user)
                self.assertIsInstance(output, tuple)
                self.assertEqual(len(output), 2)

                first, second = output
                self.assertEqual(first, user["name"])
                self.assertEqual(second, user["age"])

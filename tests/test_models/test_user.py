#!/usr/bin/python3
""" this module has TestCase of the User class """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def testEmail(self):
        user_email = User.email
        self.assertIsNotNone(user_email, "email is None")

    def testPassword(self):
        obj_password = User.password
        self.assertIsNotNone(obj_password, "password is None")

    def testFirstName(self):
        obj_first_name = User.first_name
        self.assertIsNotNone(obj_first_name, "first_name is None")

    def testLastName(self):
        obj_last_name = User.last_name
        self.assertIsNotNone(obj_last_name, "last_name is None")


if __name__ == "__main__":
    unittest.main()

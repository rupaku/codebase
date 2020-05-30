from phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("bob","12345")
        number= phonebook.lookup("bob")
        self.assertEqual("12345",number)

    def test_missing_name(self):
        phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

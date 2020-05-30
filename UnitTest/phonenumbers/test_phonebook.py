from phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook =PhoneBook()

    def tearDown(self):
        pass

    def test_lookup_by_name(self):
        #phonebook = PhoneBook()
        self.phonebook.add("bob","12345")
        number= self.phonebook.lookup("bob")
        self.assertEqual("12345",number)

    def test_missing_name(self):
        #phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

from phonebook import PhoneBook
import unittest

class PhoneBookTest(unittest.TestCase):
    #Arrang -Act-Assert
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

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Anna","012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Bob","12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob","1234")
        self.phonebook.add("Sue","123")
        self.assertTrue(self.phonebook.is_consistent())

    def tets_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue","123343")
        self.assertIn("Sue",self.phonebook.get_names())
        self.aseertIn("123343",self.phonebook.get_numbers())
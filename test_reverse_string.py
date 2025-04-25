import unittest
from reverse_string import reverse_string

class TestReverseString(unittest.TestCase):

    # Normal test cases
    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_word_with_spaces(self):
        self.assertEqual(reverse_string("text wise"), "esiw txet")

    # Edge test cases
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#"), "#@!")

if __name__ == "__main__":
    unittest.main()

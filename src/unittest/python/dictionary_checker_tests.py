import unittest

from dictionary_checker import DictionaryChecker


class HelloWorldTest(unittest.TestCase):
    dict_checker = DictionaryChecker()

    def test_word_in_dictionary_successful(self):
        self.assertTrue(self.dict_checker.check_word_in_dictionary("apple"))
        self.assertTrue(self.dict_checker.check_word_in_dictionary("bone"))


    def test_word_not_in_dictionary(self):
        self.assertFalse(self.dict_checker.check_word_in_dictionary("asdfasdf"))


    def test_word_in_dict_starts_with_letters(self):
        self.assertTrue(self.dict_checker.check_if_word_starts_with_letters("app"))
        self.assertTrue(self.dict_checker.check_if_word_starts_with_letters("aardv"))


    def test_word_in_dict_does_not_start_with_letters(self):
        self.assertFalse(self.dict_checker.check_if_word_starts_with_letters("abcc"))
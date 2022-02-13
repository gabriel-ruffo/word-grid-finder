import sys
import unittest

sys.path.append("C:/Users/gabri/OneDrive/Documents/PersonalProjects/word-grid-finder/src/main/python/")

from word_finder import WordFinder


class WordFinderTests(unittest.TestCase):
    def test_one_line(self):
        expected_words = ["cab", "bac"]
        word_finder = WordFinder("one_line.txt")
        found_words = word_finder.generate_word_list()
        self.assertCountEqual(expected_words, found_words)
        
    def test_one_line_x(self):
        expected_words = ["cab", "bac"]
        word_finder = WordFinder("one_line_x.txt")
        found_words = word_finder.generate_word_list()
        self.assertCountEqual(expected_words, found_words)
        
    def test_one_line_s(self):
        expected_words = ["cab", "cabs", "abs", "bac"]
        word_finder = WordFinder("one_line_s.txt")
        found_words = word_finder.generate_word_list()
        self.assertCountEqual(expected_words, found_words)
        
    def test_empty_letters(self):
        expected_words = ["cab", "bac"]
        word_finder = WordFinder("empty_letters.txt")
        found_words = word_finder.generate_word_list()
        self.assertCountEqual(expected_words, found_words)
        
        
if __name__ == '__main__':
    unittest.main()
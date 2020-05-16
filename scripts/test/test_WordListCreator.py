# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.WordListCreator import WordListCreator

class test_WordListCreator(unittest.TestCase):

    scenarios_get_words = [
        ([], []),
        (["\n"], []),
        (["# any line starting with hash"], []),
        (["aaaa\n"], ["aaaa"]),
        (["aaaa\n", "bbbb\n"], ["aaaa", "bbbb"]),
        (["aaaa,bbbb\n"], ["aaaa", "bbbb"]),
        (["aaaa,bbbb,cccc\n"], ["aaaa", "bbbb", "cccc"])
    ]
    def test_get_words(self):
        for lines, expected_list_of_words in self.scenarios_get_words:
            with self.subTest():
                self.assertEqual(expected_list_of_words, WordListCreator().get_words(lines))

if __name__ == '__main__':
    unittest.main()

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
                self.assertEqual(
                    expected_list_of_words,
                    WordListCreator().get_words(lines)
                )

    scenarios_extract_words_with_unique_first_4_characters = [
        (set(["aaaa"]), set(["aaaa"])),
        (set(["aaaa", "bbbb"]), set(["aaaa", "bbbb"])),
        (set(["aaaa", "bbbb", "cccc"]), set(["aaaa", "bbbb", "cccc"])),
        (set(["aaaa", "aaaab"]), set(["aaaa"])),
        (set(["aaaa", "bbbb", "cccc", "aaaab", "bbbba", "bbbbb", "cccca", "ccccb", "ccccc"]), set(["aaaa", "bbbb", "cccc"])),
    ]
    def test_extract_words_with_unique_first_4_characters(self):
        for word_set, expected_word_set in self.scenarios_extract_words_with_unique_first_4_characters:
            with self.subTest():
                self.assertEqual(
                    expected_word_set,
                    WordListCreator().extract_words_with_unique_first_4_characters(word_set)
                )

if __name__ == '__main__':
    unittest.main()

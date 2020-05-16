# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.CharacterSetUtils import CharacterSetUtils
from scripts.test.TestConstants import BASE_CHARACTER_SETS, CHARACTER_SET_DESCRIPTION_ENGLISH, \
    CHARACTER_SET_ENGLISH, CHARACTER_SET_DESCRIPTION_POLISH, CHARACTER_SET_POLISH


class test_CharacterSetUtils(unittest.TestCase):

    correct_scenarios_character_set = [
        [BASE_CHARACTER_SETS,
         CHARACTER_SET_DESCRIPTION_ENGLISH,
         CHARACTER_SET_ENGLISH],

        [BASE_CHARACTER_SETS,
         CHARACTER_SET_DESCRIPTION_POLISH,
         CHARACTER_SET_POLISH]
    ]

    def test_get_character_set(self):
        for base_character_sets, character_set_description, expected_character_set in self.correct_scenarios_character_set:
            with self.subTest():
                self.assertEqual(
                    expected_character_set,
                    CharacterSetUtils().get_character_set(base_character_sets, character_set_description)
                )

    scenarios_map_word = [
        [CHARACTER_SET_DESCRIPTION_ENGLISH, "worad", "worad"],
        [CHARACTER_SET_DESCRIPTION_ENGLISH, "worbd", "worbd"],
        [CHARACTER_SET_DESCRIPTION_ENGLISH, "worcd", "worcd"],
        [CHARACTER_SET_DESCRIPTION_ENGLISH, "wordd", "wordd"],

        [CHARACTER_SET_DESCRIPTION_POLISH, "zażółć", "zazolc"],
        [CHARACTER_SET_DESCRIPTION_POLISH, "gęślą", "gesla"],
        [CHARACTER_SET_DESCRIPTION_POLISH, "jaźń", "jazn"],
    ]

    def test_map_word(self):
        for character_set_description, word, expected_word_mapped in self.scenarios_map_word:
            with self.subTest():
                word_mapped = CharacterSetUtils().map_word(character_set_description, word)
                self.assertEqual(expected_word_mapped, word_mapped)

    scenarios_map_words = [
        [CHARACTER_SET_DESCRIPTION_POLISH,
         ["zażółć", "gęślą", "jaźń"],
         {"zazolc": ["zażółć"], "gesla": ["gęślą"], "jazn":["jaźń"]}],

        [CHARACTER_SET_DESCRIPTION_POLISH,
         ["zażółć", "gęślą", "jaźń", "jaźn", "jazn"],
         {"zazolc": ["zażółć"], "gesla": ["gęślą"], "jazn":["jaźń", "jaźn", "jazn"]}],

        [CHARACTER_SET_DESCRIPTION_POLISH,
         ["zażółć", "gęślą", "jaźń", "zazolc", "gęśla", "jaźn", "jazn"],
         {"zazolc": ["zażółć", "zazolc"], "gesla": ["gęślą", "gęśla"], "jazn":["jaźń", "jaźn", "jazn"]}]
    ]
    def test_map_words(self):
        for character_set_description, words, expected_words_mapped in self.scenarios_map_words:
            with self.subTest():
                words_mapped = CharacterSetUtils().map_words(character_set_description, words)

                self.assertEqual(expected_words_mapped, words_mapped)


if __name__ == '__main__':
    unittest.main()

# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.CharacterSetUtils import CharacterSetUtils
from scripts.test.TestConstants import CHARACTER_SETS, CHARACTER_SET_DESCRIPTION_ENGLISH, \
    CHARACTER_SET_ENGLISH, CHARACTER_SET_DESCRIPTION_POLISH, CHARACTER_SET_POLISH


class TestCharacterSetUtils(unittest.TestCase):

    correct_scenarios_character_set = [
        [CHARACTER_SETS,
         CHARACTER_SET_DESCRIPTION_ENGLISH,
         CHARACTER_SET_ENGLISH],

        [CHARACTER_SETS,
         CHARACTER_SET_DESCRIPTION_POLISH,
         CHARACTER_SET_POLISH]
    ]

    def test_get_character_set(self):
        for character_sets, character_set, expected_character_set in self.correct_scenarios_character_set:
            with self.subTest():
                self.assertEqual(
                    expected_character_set,
                    CharacterSetUtils().get_character_set(character_sets, character_set)
                )

    scenarios_map_word = [
        [CHARACTER_SET_DESCRIPTION_ENGLISH,
         ["worad", "worbd", "worcd", "wordd"],
         ["worad", "worbd", "worcd", "wordd"]],

        [CHARACTER_SET_DESCRIPTION_POLISH,
         ["zażółć", "gęślą", "jaźń"],
         ["zazolc", "gesla", "jazn"]]
    ]

    def test_map_word(self):
        for character_set, words, expected_words_mapped in self.scenarios_map_word:
            with self.subTest():
                word_list_mapped = []
                for word in words:
                    word_mapped = CharacterSetUtils().map_word(character_set, word)
                    word_list_mapped.append(word_mapped)

                self.assertListEqual(expected_words_mapped, word_list_mapped)


if __name__ == '__main__':
    unittest.main()

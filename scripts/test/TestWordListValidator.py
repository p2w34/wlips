# This Python file uses the following encoding: utf-8
import unittest

from scripts.WordList import WordList
from scripts.WordListValidator import WordListValidator

class TestWordListValidator(unittest.TestCase):

    ENGLISH_CHARACTERS = [c for c in "abcdefghijklmnopqrstuvwxyz"]
    ENGLISH_CHARACTER_SET = {"english": ENGLISH_CHARACTERS}

    incorrect_scenarios_file_name = [
        ["12345678", "just_language_name_without_hash"],
        ["12345678", "12345678_hash_on_wrong_position"],
        ["12345678", "12345678_hash_on_wrong_position-additional_description"],
        ["12345678", "language_name-1234567-hash_too_short"],
        ["12345678", "language_name-123456788-hash_too_long"],
        ["12345678", "language_name-12345678g-wrong_char_in_hash"],
        ["12345678", "language_name-12345678-additional_description-redundant_part"],
        ["12345678", str.ljust("language_name-12345678-file_name_too_long", WordListValidator.FILE_NAME_MAX_LENGTH + 1, 'x')]
    ]
    def test_incorrect_is_file_name_valid(self):
        for expected_file_hash, file_name in self.incorrect_scenarios_file_name:
            with self.subTest():
                self.assertFalse(WordListValidator({}, WordList([], {}, [], {expected_file_hash:file_name})).is_file_name_valid())

    correct_scenarios_file_name = [
        ["12345678", "english-12345678"],
        ["abcdef12", "english-abcdef12"],
        ["12345678", "english-12345678-additional_description"],
        ["12345678", str.ljust("language_name-12345678-", WordListValidator.FILE_NAME_MAX_LENGTH, 'x')],
        ["12345678", str.ljust("language_name-12345678-additional_description", WordListValidator.FILE_NAME_MAX_LENGTH, 'x')],
    ]
    def test_correct_is_file_name_syntax(self):
        for expected_file_hash, file_name in self.correct_scenarios_file_name:
            with self.subTest():
                self.assertTrue(WordListValidator({}, WordList([], {}, [], {expected_file_hash:file_name})).is_file_name_valid())

    correct_scenarios_character_set = [
        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["wordone", "wordtwo", "wordthree"], {}),
         ENGLISH_CHARACTERS],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}, ["zażółć", "gęślą", "jaźń"], {}),
         ENGLISH_CHARACTERS + ['ą','ć','ę','ł','ń','ó','ś','ź','ż']]
    ]
    def test_get_character_set(self):
        for character_sets, word_list, expected_character_set in self.correct_scenarios_character_set:
            with self.subTest():
                self.assertEqual(WordListValidator(character_sets, word_list).get_character_set(), expected_character_set)

    def test_correct_is_character_set_valid(self):
        for character_sets, word_list, expected_character_set in self.correct_scenarios_character_set:
            with self.subTest():
                self.assertTrue(WordListValidator(character_sets, word_list).is_character_set_valid())

    not_allowed_character='ą'
    incorrect_scenarios_character_set = [
        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["word"+not_allowed_character], {}),
         ENGLISH_CHARACTERS],
    ]
    def test_incorrect_is_character_set_valid(self):
        for character_sets, word_list, expected_character_set in self.incorrect_scenarios_character_set:
            with self.subTest():
                self.assertFalse(WordListValidator(character_sets, word_list).is_character_set_valid())

    def test_correct_is_word_length_valid(self):
        word_list = WordList("english", {}, ["word", "worda", "wordab", "wordabc", "wordabcd"], {})
        self.assertTrue(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_word_length_valid())

    incorrect_scenarios_word_length = [
        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["wor"], {})],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["wordabcde"], {})]
    ]
    def test_incorrect_is_word_length_invalid(self):
        for character_sets, word_list in self.incorrect_scenarios_word_length:
            with self.subTest():
                self.assertFalse(WordListValidator(character_sets, word_list).is_word_length_valid())

    def test_correct_is_number_of_words_valid(self):
        word_list = WordList("english", {}, self.create_word_list_of_length(2048), {})
        self.assertTrue(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_number_of_words_valid())

    def test_incorrect_is_number_of_words_valid(self):
        word_list = WordList("english", {}, self.create_word_list_of_length(2047), {})
        self.assertFalse(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_number_of_words_valid())

        word_list = WordList("english", {}, self.create_word_list_of_length(2049), {})
        self.assertFalse(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_number_of_words_valid())

    def test_correct_is_list_of_words_sorted(self):
        word_list = WordList("english", {}, ["worda", "wordb", "wordc"], {})
        self.assertTrue(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_list_of_words_sorted())

    def test_incorrect_is_list_of_words_sorted(self):
        word_list = WordList("english", {}, ["wordc", "wordb", "worda"], {})
        self.assertFalse(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_list_of_words_sorted())

    def test_correct_is_first_4_letter_unique(self):
        word_list = WordList("english", {}, ["worad", "worbd", "worcd", "wordd"], {})
        self.assertTrue(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_first_4_characters_unique())

    def test_correct_is_first_4_letter_unique(self):
        word_list = WordList("english", {}, ["wordd", "wordd"], {})
        self.assertFalse(WordListValidator(self.ENGLISH_CHARACTER_SET, word_list).is_first_4_characters_unique())

    scenarios_map_word = [
        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["worad", "worbd", "worcd", "wordd"], {}),
         ["worad", "worbd", "worcd", "wordd"]],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'}, ["zażółć", "gęślą", "jaźń"], {}),
        ["zazolc", "gesla", "jazn"]]
    ]
    def test_map_word(self):
        for character_sets, word_list, expected_mapped_word_list in self.scenarios_map_word:
            with self.subTest():
                word_list_validator = WordListValidator(character_sets, word_list)
                word_list_mapped = []
                for word in word_list.word_list:
                    word_mapped = word_list_validator.map_word(word)
                    word_list_mapped.append(word_mapped)

                self.assertListEqual(word_list_mapped, expected_mapped_word_list)

    scenarios_levenshtein = [
        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["aaaa", "aabb", "aaaabb", "bbaaaa"], {}),
         []],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["aaaa", "aaab"], {}),
         ['CREATE (aaaa:word {value: "aaaa"})',
          'CREATE (aaab:word {value: "aaab"})',
          'CREATE (aaaa)-[:D]->(aaab)']],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {}, ["aaaa", "aaab", "caaa"], {}),
         ['CREATE (aaaa:word {value: "aaaa"})',
          'CREATE (aaab:word {value: "aaab"})',
          'CREATE (caaa:word {value: "caaa"})',
          'CREATE (aaaa)-[:D]->(aaab)',
          'CREATE (aaaa)-[:D]->(caaa)']],

        [ENGLISH_CHARACTER_SET,
         WordList("english", {'ą':'a'}, ["aaaa", "aaąą", "ąąaa", "bbbb"], {}),
         ['CREATE (aaaa:word {value: "aaaa"})',
          'CREATE (aaąą:word {value: "aaąą"})',
          'CREATE (ąąaa:word {value: "ąąaa"})',
          'CREATE (aaaa)-[:D]->(aaąą)',
          'CREATE (aaaa)-[:D]->(ąąaa)',
          'CREATE (aaąą)-[:D]->(ąąaa)']],
    ]
    def test_get_neo4j_graph_with_levenshtein_distances(self):
        for character_sets, word_list, expected_neo4j_graph in self.scenarios_levenshtein:
            with self.subTest():
                neo4j_graph = WordListValidator(character_sets, word_list).get_neo4j_graph_with_levenshtein_distances()
                self.assertListEqual(neo4j_graph, expected_neo4j_graph)

    def create_word_list_of_length(self, no_of_words):
        word = "word"
        words = []
        for w in range(no_of_words):
            words.append(word)
        return words

if __name__ == '__main__':
    unittest.main()

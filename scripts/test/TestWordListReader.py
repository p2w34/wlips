# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.WordListReader import WordListReader
from scripts.src.WordList import WordList

class TestWordListReader(unittest.TestCase):

    SAMPLE_WORD_LIST = "sample_word_list"

    def test_correct_validate_file_exists(self):
        WordListReader().validate_file_exists(self.SAMPLE_WORD_LIST)

    def test_incorrect_validate_file_exists(self):
        NON_EXISTING_WORD_LIST = "non_existing_word_list"
        with self.assertRaises(SystemExit):
            WordListReader().validate_file_exists(NON_EXISTING_WORD_LIST)

    def test_get_file_hash_info(self):
        expected_file_hash_info = {"3b784e25": self.SAMPLE_WORD_LIST}
        file_hash_info = WordListReader().get_file_hash_info(self.SAMPLE_WORD_LIST)
        self.assertEqual(file_hash_info, expected_file_hash_info)

    def test_read_file(self):
        expected_lines = [
            "[english-qvx+ą:a+ć:c+ę:e+ł:l+ń:n+ó:o+ś:s+ź:z+ż:z]\n",
            "awokado\n",
            "banan\n",
            "tygrys\n"
        ]
        lines = WordListReader().read_file(self.SAMPLE_WORD_LIST)
        self.assertListEqual(expected_lines, lines)

    correct_scenarios_first_line = [
        ("[english]", "english", [], {}),
        ("[english+ą:a]", "english", [], {"ą":"a"}),
        ("[english-q]", "english", ['q'], {}),
        ("[english-qv]", "english", ['q', 'v'], {}),
        ("[english-qvx]", "english", ['q', 'v', 'x'], {}),
        ("[english-qvx+ą:a]", "english", ['q', 'v', 'x'], {"ą":"a"}),
        ("[english-qvx+ą:a+ć:c]", "english", ['q', 'v', 'x'], {"ą":"a", "ć":"c"}),
        ("[english-qvx+ą:a+ć:c+ę:e]", "english", ['q', 'v', 'x'], {"ą":"a", "ć":"c", "ę":"e"})
    ]
    def test_correct_first_line_syntax(self):
        for input_line,\
            expected_base_character_set,\
            expected_redundant_character_set,\
            expected_extra_character_set \
            in self.correct_scenarios_first_line:
            with self.subTest():
                base_character_set,\
                redundant_character_set,\
                extra_character_set = WordListReader().parse_first_line(input_line)

                self.assertEqual(expected_base_character_set, base_character_set)
                self.assertListEqual(expected_redundant_character_set, redundant_character_set)
                self.assertEqual(expected_extra_character_set, extra_character_set)

    incorrect_scenarios_first_line = [
        'english',
        '[english',
        'english]',
        'english+',
        '[english+]',
        '[english-]',
        'a[english]',
        '[english]a',
        '[english+ą|a]',
        '[english-q-]',
        '[english-q-v]',
        '[english+ą:+ć:c]',
        '[english+ą:a-q]',
        '[english:ą:a+ć:c+ę:e]',
        '[english+ą:aa]'
    ]
    def test_incorrect_first_line_syntax(self):
        for input_line in self.incorrect_scenarios_first_line:
            with self.subTest():
                self.assertRaisesRegex(Exception,
                                       "invalid first line syntax",
                                       WordListReader().parse_first_line,
                                       input_line)

    correct_scenarios_lines = [
        (["firstline\n"], []),
        (["firstline\n", "word1\n"], ["word1"]),
        (["firstline\n", "word1\n", "word2\n", "word3\n"], ["word1", "word2", "word3"])
    ]
    def test_correct_parse_word_list(self):
        for lines, expected_word_list in self.correct_scenarios_lines:
            with self.subTest():
                word_list = WordListReader().parse_word_list(lines)
                self.assertListEqual(expected_word_list, word_list)

    incorrect_scenarios_lines = [
        ["firstline"],
        ["firstline\n", "word1"],
        ["firstline", "\n", "word2\n"],
        ["firstline\n", "word1\n", "word2\n", "\n"]
    ]
    def test_incorrect_parse_word_list(self):
        for lines in self.incorrect_scenarios_lines:
            with self.subTest():
                self.assertRaises(Exception,
                                  WordListReader().parse_word_list,
                                  lines)

    def test_parse_file(self):
        character_set = {
            WordList.BASE_CHARACTER_SET: "english",
            WordList.REDUNDANT_CHARACTER_SET: ['q','v','x'],
            WordList.EXTRA_CHARACTER_SET: {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'},
        }
        EXPECTED_WORD_LIST = WordList(character_set,
                                      ["awokado", "banan", "tygrys"],
                                      {"3b784e25": self.SAMPLE_WORD_LIST})
        word_list = WordListReader().parse_file(self.SAMPLE_WORD_LIST)
        self.assertEqual(EXPECTED_WORD_LIST, word_list)

if __name__ == '__main__':
    unittest.main()

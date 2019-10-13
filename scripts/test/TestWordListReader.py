# This Python file uses the following encoding: utf-8
import unittest

from scripts.WordListReader import WordListReader
from scripts.WordList import WordList

class TestWordListReader(unittest.TestCase):

    def test_correct_validate_file_exists(self):
        EXISTING_PATH = "./sample_word_list"
        WordListReader().validate_file_exists(EXISTING_PATH)

    def test_incorrect_validate_file_exists(self):
        NON_EXISTING_PATH = "./non_existing_word_list"
        with self.assertRaises(SystemExit):
            WordListReader().validate_file_exists(NON_EXISTING_PATH)

    def test_read_file(self):
        SAMPLE_WORD_LIST = "./sample_word_list"
        expected_lines = [
            "[english+ą:a+ć:c+ę:e+ł:l+ń:n+ó:o+ś:s+ź:z+ż:z]\n",
            "awokado\n",
            "banan\n",
            "tygrys\n"
        ]
        lines = WordListReader().read_file(SAMPLE_WORD_LIST)
        self.assertListEqual(expected_lines, lines)

    correct_scenarios_first_line = [
        ("[english]", "english", {}),
        ("[english+ą:a]", "english", {"ą":"a"}),
        ("[english+ą:a+ć:c]", "english", {"ą":"a", "ć":"c"}),
        ("[english+ą:a+ć:c+ę:e]", "english", {"ą":"a", "ć":"c", "ę":"e"})
    ]
    def test_correct_first_line_syntax(self):
        for input_line, expected_character_set, expected_mappings in self.correct_scenarios_first_line:
            with self.subTest():
                character_set, mappings = WordListReader().parse_first_line(input_line)
                self.assertEqual(expected_character_set, character_set)
                self.assertEqual(expected_mappings, mappings)

    incorrect_scenarios_first_line = [
        'english',
        '[english',
        'english]',
        'english+',
        '[english+]',
        'a[english]',
        '[english]a',
        '[english+ą|a]',
        '[english+ą:+ć:c]',
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
        EXPECTED_WORD_LIST = WordList("english",
                                      {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z'},
                                      ["awokado", "banan", "tygrys"])
        SAMPLE_WORD_LIST = "./sample_word_list"
        word_list = WordListReader().parse_file(SAMPLE_WORD_LIST)
        self.assertEqual(EXPECTED_WORD_LIST, word_list)

if __name__ == '__main__':
    unittest.main()

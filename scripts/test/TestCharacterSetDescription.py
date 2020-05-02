# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.CharacterSetDescription import CharacterSetDescription


class TestCharacterSet(unittest.TestCase):
    correct_character_set_description = [
        ("[english]", "english", [], {}),
        ("some random letters before [english]", "english", [], {}),
        ("[english] some random letters after", "english", [], {}),
        ("# some random letters before [english] and after", "english", [], {}),
        ("[english+ą:a]", "english", [], {"ą": "a"}),
        ("[english-q]", "english", ['q'], {}),
        ("[english-qv]", "english", ['q', 'v'], {}),
        ("[english-qvx]", "english", ['q', 'v', 'x'], {}),
        ("[english-qvx+ą:a]", "english", ['q', 'v', 'x'], {"ą": "a"}),
        ("[english-qvx+ą:a+ć:c]", "english", ['q', 'v', 'x'], {"ą": "a", "ć": "c"}),
        ("[english-qvx+ą:a+ć:c+ę:e]", "english", ['q', 'v', 'x'], {"ą": "a", "ć": "c", "ę": "e"})
    ]

    def test_correct_character_set_description(self):
        for character_set_description, \
            expected_base_character_set, \
            expected_redundant_character_set, \
            expected_mappings \
                in self.correct_character_set_description:
            with self.subTest():
                character_set = CharacterSetDescription(character_set_description)

                self.assertEqual(expected_base_character_set, character_set.base_character_set)
                self.assertListEqual(expected_redundant_character_set, character_set.redundant_character_set)
                self.assertEqual(expected_mappings, character_set.mappings)

    incorrect_character_set_description = [
        'english',
        '[english',
        'english]',
        'english+',
        '[english+]',
        '[english-]',
        '[english+ą|a]',
        '[english-q-]',
        '[english-q-v]',
        '[english+ą:+ć:c]',
        '[english+ą:a-q]',
        '[english:ą:a+ć:c+ę:e]',
        '[english+ą:aa]'
    ]

    def test_incorrect_character_set_description(self):
        for character_set_description in self.incorrect_character_set_description:
            with self.subTest():
                with self.assertRaises(Exception):
                    CharacterSetDescription(character_set_description)


if __name__ == '__main__':
    unittest.main()

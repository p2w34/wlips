# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.WordListCreator import WordListCreator

class TestWordListCreator(unittest.TestCase):

    scenarios_create_map_of_neighbours = [
        (["aaaa"], {"aaaa":[]}),
        (["aaaa", "bbbb"], {"aaaa":[], "bbbb":[]}),
        (["aaaa", "aaab"], {"aaaa":["aaab"], "aaab":["aaaa"]}),
        (["aaaa", "baaa", "abaa", "aaba", "aaab", "ffff"], {"aaaa":["baaa", "abaa", "aaba", "aaab"], "baaa":["aaaa"], "abaa":["aaaa"], "aaba":["aaaa"], "aaab":["aaaa"], "ffff":[]})
    ]
    def test_create_map_of_neighbours(self):
        for words, expected_map_of_neighbours in self.scenarios_create_map_of_neighbours:
            with self.subTest():
                self.assertEqual(expected_map_of_neighbours, WordListCreator().create_map_of_neighbours(words))

    scenarios_create_sets_of_neighbours = [
        ({"aaaa":[]}, {frozenset(["aaaa"])}),

        ({"aaaa":[], "bbbb":[]}, {frozenset(["aaaa"]), frozenset(["bbbb"])}),

        ({"aaaa":["aaab"], "aaab":["aaaa"]}, {frozenset(["aaaa", "aaab"])}),

        ({"aaaa":["baaa", "abaa", "aaba", "aaab"], "baaa":["aaaa"], "abaa":["aaaa"], "aaba":["aaaa"], "aaab":["aaaa"], "ffff":[]},
         {frozenset(["aaaa", "baaa", "abaa", "aaba", "aaab"]), frozenset(["ffff"])}),

        ({"aaaa":["aaab"], "aaab":["aaaa"], "babb":["baab"], "baab":["babb", "aaab"]}, {frozenset(["aaaa", "aaab", "baab", "babb"])}),
    ]
    def test_create_sets_of_neighbours(self):
        for map_of_neighbours, expected_sets_of_neighbours in self.scenarios_create_sets_of_neighbours:
            with self.subTest():
                self.assertEqual(expected_sets_of_neighbours, WordListCreator().create_sets_of_neighbours(map_of_neighbours))

if __name__ == '__main__':
    unittest.main()

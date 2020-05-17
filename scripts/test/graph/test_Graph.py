# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.graph.Graph import Graph
from scripts.src.WordNeighbourhoodStrategy import WordNeighbourhoodStrategy


class test_Graph(unittest.TestCase):

    scenarios_create_map_of_neighbours = [
        (["aaaa"], {"aaaa": set()}),
        (["aaaa", "bbbb"], {"aaaa":set(), "bbbb":set()}),
        (["aaaa", "aaab"], {"aaaa":set(["aaab"]), "aaab":set(["aaaa"])}),
        (["aaaa", "baaa", "abaa", "aaba", "aaab", "ffff"], {"aaaa":set(["baaa", "abaa", "aaba", "aaab"]), "baaa":set(["aaaa"]), "abaa":set(["aaaa"]), "aaba":set(["aaaa"]), "aaab":set(["aaaa"]), "ffff":set()})
    ]
    def test_create_map_of_neighbours(self):
        for words, expected_map_of_neighbours in self.scenarios_create_map_of_neighbours:
            with self.subTest():
                self.assertEqual(
                    expected_map_of_neighbours,
                    Graph(WordNeighbourhoodStrategy()).create_map_of_neighbours(words)
                )

    scenarios_create_sets_of_neighbours = [
        ({"aaaa":set()}, {frozenset(["aaaa"])}),

        ({"aaaa":set(), "bbbb":set()}, {frozenset(["aaaa"]), frozenset(["bbbb"])}),

        ({"aaaa":set(["aaab"]), "aaab":set(["aaaa"])}, {frozenset(["aaaa", "aaab"])}),

        ({"aaaa":set(["baaa", "abaa", "aaba", "aaab"]), "baaa":set(["aaaa"]), "abaa":set(["aaaa"]), "aaba":set(["aaaa"]), "aaab":set(["aaaa"]), "ffff":set()},
         {frozenset(["aaaa", "baaa", "abaa", "aaba", "aaab"]), frozenset(["ffff"])}),

        ({"aaaa":set(["aaab"]), "aaab":set(["aaaa"]), "babb":set(["baab"]), "baab":set(["babb", "aaab"])}, {frozenset(["aaaa", "aaab", "baab", "babb"])}),
    ]
    def test_create_sets_of_neighbours(self):
        for map_of_neighbours, expected_sets_of_neighbours in self.scenarios_create_sets_of_neighbours:
            with self.subTest():
                self.assertEqual(
                    expected_sets_of_neighbours,
                    Graph(WordNeighbourhoodStrategy()).split_into_isolated_sets_of_neighbours(map_of_neighbours)
                )

    scenarios___get_first_word_with_max_number_of_neighbours = [
        (set(["aaaa"]), ("aaaa", 0)),
        (set(["aaaa", "bbbb"]), ("aaaa", 0)),
        (set(["aaaa", "bbbb", "cccc"]), ("aaaa", 0)),
        (set(["aaaa", "aaab"]), ("aaaa", 1)),
        (set(["aaaa", "aaab", "baab"]), ("aaab", 2)),
        (set(["aaaa", "aaab", "baab", "bbab", "bbbb", "baac"]), ("baab", 3)),
        (set(["aaaa", "aaab", "aaac", "baac", "baad", "baae"]), ("aaac", 3)),
    ]
    def test___get_first_word_with_max_number_of_neighbours(self):
        for set_of_neighbours, expected_word_with_max_number_of_neighbours in self.scenarios___get_first_word_with_max_number_of_neighbours:
            with self.subTest():
                self.assertEqual(
                    expected_word_with_max_number_of_neighbours,
                    Graph(WordNeighbourhoodStrategy())._Graph__get_first_word_with_max_number_of_neighbours(set_of_neighbours)
                )

    scenarios_extract_largest_set_without_neighbours_from_set = [
        (set(["aaaa"]), set(["aaaa"])),
        (set(["aaaa", "bbbb"]), set(["aaaa", "bbbb"])),
        (set(["aaaa", "bbbb", "cccc"]), set(["aaaa", "bbbb", "cccc"])),
        (set(["aaaa", "aaab"]), set(["aaab"])),
        (set(["aaaa", "aaab", "baab"]), set(["aaaa", "baab"])),
        (set(["aaaa", "aaab", "aaac"]), set(["aaac"])),
        (set(["aaaa", "aaab", "aaac", "aaad"]), set(["aaad"])),
        (set(["aaaa", "aaab", "aaac", "aaad", "aaae"]), set(["aaae"])),
    ]
    def test_extract_largest_set_without_neighbours_from_set(self):
        for set_of_neighbours, expected_largest_set_without_neighbours in self.scenarios_extract_largest_set_without_neighbours_from_set:
            with self.subTest():
                self.assertEqual(
                    expected_largest_set_without_neighbours,
                    Graph(WordNeighbourhoodStrategy()).extract_largest_set_without_neighbours_from_set(set_of_neighbours)
                )


if __name__ == '__main__':
    unittest.main()

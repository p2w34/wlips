# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.GraphUtils import GraphUtils


class TestGraphUtils(unittest.TestCase):

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
                self.assertEqual(expected_sets_of_neighbours, GraphUtils().create_sets_of_neighbours(map_of_neighbours))


if __name__ == '__main__':
    unittest.main()

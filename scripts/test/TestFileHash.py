# This Python file uses the following encoding: utf-8
import unittest

from scripts.src.FileHash import FileHash

class TestFileHash(unittest.TestCase):

    expected_hash = "3b784e25"

    def test_compute_file_hash(self):
        file_hash = FileHash().compute_file_hash("./sample_word_list")
        self.assertEqual(self.expected_hash, file_hash)

    def test_compute_hash(self):
        character_set_description = "[english-qvx+ą:a+ć:c+ę:e+ł:l+ń:n+ó:o+ś:s+ź:z+ż:z]"
        word_list = ["awokado", "banan", "tygrys"]

        hash = FileHash().compute_hash(character_set_description, word_list)
        self.assertEqual(self.expected_hash, hash)

if __name__ == '__main__':
    unittest.main()

import os
import sys

from scripts.src.CharacterSetDescription import CharacterSetDescription
from scripts.src.CharacterSetUtils import CharacterSetUtils
from scripts.src.file.FileHash import FileHash
from scripts.src.graph.Graph import Graph
from scripts.src.WordList import WordList
from scripts.src.WordNeighbourhoodStrategy import WordNeighbourhoodStrategy


class WordListCreator:

    def create_word_list(self, file_path, base_character_sets):
        self.validate_file_exists(file_path)
        lines = self.read_file(file_path)
        words = self.get_words(lines)
        character_set_description = CharacterSetDescription(lines[0])
        words_mapped = CharacterSetUtils().map_words(character_set_description, words)
        print("Words mapping with duplicates: ", words_mapped)
        list_of_words = self.create_list(words_mapped.keys())
        file_hash = FileHash().compute_hash("[english]", list_of_words)
        return WordList(character_set_description, list_of_words, file_hash)

    def validate_file_exists(self, file_path):
        if not os.path.isfile(file_path):
            print("File path {} does not exist. Exiting...".format(file_path))
            sys.exit()

    def read_file(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
        return lines

    def get_words(self, lines):
        words = []
        for line in lines:
            if line == "\n":
                continue
            if line[0] == "#":
                continue
            words = words + line[:-1].split(",")

        return words

    def create_list(self, words):
        print("Number of all words: ", len(words))

        words2 = set()
        for w in words:
            if len(w) >= 4 and len(w) <=8:
                words2.add(w)
        print("Number of words with 4-8 chars: ", len(words2))

        graph_utils = Graph(WordNeighbourhoodStrategy())
        word_set = graph_utils.extract_largest_set_without_neighbours_from_raw_set(words2)
        word_list = list(word_set)
        word_list.sort()
        return word_list

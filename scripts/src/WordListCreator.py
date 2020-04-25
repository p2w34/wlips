import os
import sys

from Levenshtein import distance

class WordListCreator:

    def create_word_list(self, file_path):
        self.validate_file_exists(file_path)
        lines = self.read_file(file_path)
        words = self.get_words(lines)
        word_list = self.create_list(words)
        return word_list

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
            words.append(line[:-1])

        return words

    def create_list(self, words):
        print("Number of all words: ", len(words))

        words2 = []
        for w in words:
            if len(w) >= 4 and len(w) <=8:
                words2.append(w)
        print("Number of words with 4-8 chars: ", len(words2))

        map_of_neighbours = self.create_map_of_neighbours(words2)
        print("Map of neighbours: ", map_of_neighbours)
        sets_of_neighbours = self.create_sets_of_neighbours(map_of_neighbours)
        print("Sets of neighbours: ", sets_of_neighbours)
        print("Number of sets of neighbours: ", len(sets_of_neighbours))
        word_list = self.get_word_list(sets_of_neighbours)
        print("Word list: ", word_list)
        return word_list

    def create_map_of_neighbours(self, words):
        map_of_neighbours = {}
        for w in words:
            list_of_neighbours = []
            for w2 in words:
                if w != w2 and (distance(w[:4], w2[:4]) == 1 or w[:4] == w2[:4]):
                    list_of_neighbours.append(w2)
            map_of_neighbours.update({w: list_of_neighbours})

        return map_of_neighbours

    def create_sets_of_neighbours(self, map_of_neighbours):

        sets_of_neighbours = set()

        for word in map_of_neighbours.keys():
            # if a neighbour in already existing set - add
            # else create a new set
            word_has_neighbours = False
            set_of_neighbours_to_update = {}
            set_of_neighbours_updated = {}
            for set_of_neighbours in sets_of_neighbours:
                for word2 in set_of_neighbours:
                    if word2 in map_of_neighbours.get(word):
                        set_of_neighbours_to_update = set_of_neighbours
                        set_of_neighbours_updated = set([word]).union(set_of_neighbours)
                        word_has_neighbours = True

            if word_has_neighbours == True:
                sets_of_neighbours.remove(set_of_neighbours_to_update)
                sets_of_neighbours.update({frozenset(set_of_neighbours_updated)})
            else:
                sets_of_neighbours.add(frozenset([word]))

        return sets_of_neighbours

    def get_word_list(self, sets_of_neighbours):
        word_list = []
        for set_of_neighbours in sets_of_neighbours:
            if len(set_of_neighbours) == 1:
                word_list.append(next(iter(set_of_neighbours)))
            else:
                1 == 1
                # to implement: word_list.append(split_neighbours(set_of_neighbours))
        word_list.sort()
        return word_list
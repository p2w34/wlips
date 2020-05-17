class Graph:

    def __init__(self, neighbourhood_strategy):
        self.neighbourhood_strategy = neighbourhood_strategy

    def extract_largest_set_without_neighbours_from_raw_set(self, words):
        map_of_neighbours = self.create_map_of_neighbours(words)
        word_set = self.extract_largest_set_without_neighbours_from_raw_map(map_of_neighbours)
        return word_set

    def create_map_of_neighbours(self, words):
        map_of_neighbours = {}
        for w in words:
            neighbors = set()
            for w2 in words:
                if self.neighbourhood_strategy.is_neighbours(w, w2):
                    neighbors.add(w2)
            map_of_neighbours.update({w: neighbors})

        return map_of_neighbours

    def extract_largest_set_without_neighbours_from_raw_map(self, map_of_neighbours):
        sets_of_neighbours = self.split_into_isolated_sets_of_neighbours(map_of_neighbours)
        word_set = self.extract_largest_set_without_neighbours_from_sets(sets_of_neighbours)
        return word_set

    def split_into_isolated_sets_of_neighbours(self, map_of_neighbours):
        sets_of_neighbours = set()
        for k, v in map_of_neighbours.items():
            new_set_of_neighbours = v
            new_set_of_neighbours.add(k)
            sets_of_neighbours = self.__expand_sets_of_neighbours(sets_of_neighbours, new_set_of_neighbours)

        return sets_of_neighbours

    def __expand_sets_of_neighbours(self, sets_of_neighbours, new_set_of_neighbours):
        temp_sets = set()
        for current_set in sets_of_neighbours:
            for word in current_set:
                if word in new_set_of_neighbours:
                    new_set_of_neighbours = new_set_of_neighbours.union(current_set)
                    temp_sets.add(current_set)
                    break

        for temp_set in temp_sets:
            sets_of_neighbours.remove(temp_set)

        sets_of_neighbours.add(frozenset(new_set_of_neighbours))

        return sets_of_neighbours

    def extract_largest_set_without_neighbours_from_sets(self, sets_of_neighbours):
        word_set = set()
        for set_of_neighbours in sets_of_neighbours:
            word_subset = self.extract_largest_set_without_neighbours_from_set(set_of_neighbours)
            word_set.update(word_subset)
        return word_set

    # This is just a very basic implementation.
    # Supposedly, it is not possible to present the ideal implementation as it looks like NP hard problem.
    # However, one should be able to refactor it to yield larger set. Or at least to run it way faster.
    def extract_largest_set_without_neighbours_from_set(self, set_of_neighbours):
        word, max_number_of_neighbours = self.__get_first_word_with_max_number_of_neighbours(set_of_neighbours)
        if max_number_of_neighbours == 0:
            return set_of_neighbours

        temp_set_of_neighbours = set()
        for a in set_of_neighbours:
            temp_set_of_neighbours.add(a)

        while max_number_of_neighbours > 0:
            temp_set_of_neighbours.remove(word)
            word, max_number_of_neighbours = self.__get_first_word_with_max_number_of_neighbours(temp_set_of_neighbours)

        return temp_set_of_neighbours

    def __get_first_word_with_max_number_of_neighbours(self, set_of_neighbours):
        map_of_neighbours = self.create_map_of_neighbours(set_of_neighbours)
        list_of_words_sorted = sorted(map_of_neighbours.keys())
        result = list_of_words_sorted[0]
        max_number_of_neighbours = len(map_of_neighbours.get(result))
        for word in list_of_words_sorted[1:]:
            temp = len(map_of_neighbours.get(word))
            if temp > max_number_of_neighbours:
                max_number_of_neighbours = temp
                result = word

        return result, max_number_of_neighbours

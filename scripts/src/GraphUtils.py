class GraphUtils:

    def __init__(self, neighbourhood_strategy):
        self.neighbourhood_strategy = neighbourhood_strategy

    def create_map_of_neighbours(self, words):
        map_of_neighbours = {}
        for w in words:
            neighbors = set()
            for w2 in words:
                if self.neighbourhood_strategy.is_neighbours(w, w2):
                    neighbors.add(w2)
            map_of_neighbours.update({w: neighbors})

        return map_of_neighbours

    def extract_set_without_neighbours(self, map_of_neighbours):
        sets_of_neighbours = self.create_sets_of_neighbours(map_of_neighbours)
        print("Sets of neighbours: ", sets_of_neighbours)
        print("Number of sets of neighbours: ", len(sets_of_neighbours))
        word_set = self.extract_largest_set_without_neighbours(sets_of_neighbours)
        print("Word set: ", word_set)
        return word_set

    def create_sets_of_neighbours(self, map_of_neighbours):
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

    # this is just a very basic stub and needs to be implemented properly
    def extract_largest_set_without_neighbours(self, sets_of_neighbours):
        word_set = set()
        for set_of_neighbours in sets_of_neighbours:
            if len(set_of_neighbours) == 1:
                word_set.add(next(iter(set_of_neighbours)))
            else:
                1 == 1
                # to implement: word_list.append(split_neighbours(set_of_neighbours))
        return word_set

from Levenshtein import distance

class WordNeighbourhoodStrategy:

    def is_neighbours(self, w1, w2):
        return distance(w1, w2) == 1

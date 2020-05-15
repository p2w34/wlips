from Levenshtein import distance

class WordNeighbourhoodStrategy:

    def is_neighbours(self, w1, w2):
        return w1 != w2 and (distance(w1[:4], w2[:4]) == 1 or w1[:4] == w2[:4])
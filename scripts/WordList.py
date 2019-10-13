class WordList:
    def __init__(self, base_character_set, mappings, word_list):
        self.base_character_set = base_character_set
        self.mappings = mappings
        self.word_list = word_list

    def __eq__(self, other):
        return self.base_character_set == other.base_character_set \
               and self.mappings == other.mappings \
               and self.word_list == other.word_list

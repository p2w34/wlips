class WordList:
    def __init__(self, base_character_set, mappings, word_list, file_hash_info):
        self.base_character_set = base_character_set
        self.mappings = mappings
        self.word_list = word_list
        self.file_hash_info = file_hash_info

    def __eq__(self, other):
        return self.base_character_set == other.base_character_set \
               and self.mappings == other.mappings \
               and self.word_list == other.word_list \
               and self.file_hash_info == other.file_hash_info

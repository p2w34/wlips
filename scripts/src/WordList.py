class WordList:

    BASE_CHARACTER_SET = 'BASE_CHARACTER_SET'
    REDUNDANT_CHARACTER_SET = 'REDUNDANT_CHARACTER_SET'
    EXTRA_CHARACTER_SET = 'EXTRA_CHARACTER_SET'

    def __init__(self, character_set, word_list, file_hash_info):
        self.character_set = character_set
        self.word_list = word_list
        self.file_hash_info = file_hash_info

    def __eq__(self, other):
        return self.character_set == other.character_set \
               and self.word_list == other.word_list \
               and self.file_hash_info == other.file_hash_info

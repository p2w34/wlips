class WordList:

    def __init__(self, character_set_description, word_list, file_hash_info):
        self.character_set_description = character_set_description
        self.word_list = word_list
        self.file_hash_info = file_hash_info

    def __eq__(self, other):
        return self.character_set_description == other.character_set_description \
               and self.word_list == other.word_list \
               and self.file_hash_info == other.file_hash_info

import re
from Levenshtein import distance
from scripts.src.WordList import WordList

class WordListValidator:

    MIN_WORD_LENGTH = 4
    MAX_WORD_LENGTH = 8
    NO_OF_WORDS = 2048
    MIN_LEVENSHTEIN_DISTANCE = 2

    FILE_NAME_MAX_LENGTH = 255
    FILE_NAME_NUMBER_OF_SEGMENTS_MAX = 3

    base_character_sets = None
    word_list = None

    def __init__(self, base_character_sets, word_list):
        self.base_character_sets = base_character_sets
        self.word_list = word_list

    def validate(self):
        is_word_list_valid = False

        if not self.check(self.is_file_name_valid, "file name"):
            is_word_list_valid = False

        if not self.check(self.is_character_set_valid, "character set"):
            is_word_list_valid = False

        if not self.check(self.is_word_length_valid, "word length"):
            is_word_list_valid = False

        if not self.check(self.is_number_of_words_valid, "number of words [2048]"):
            is_word_list_valid = False

        if not self.check(self.is_list_of_words_sorted, "alphabetically sorted"):
            is_word_list_valid = False

        if not self.check(self.is_first_4_characters_unique, "first 4 characters unique"):
            is_word_list_valid = False

        neo4j_graph_input = self.get_neo4j_graph_with_levenshtein_distances()
        if not neo4j_graph_input:
            print("[+] Levenshtein distance at least once")
        else:
            print("[-] Levenshtein distance at least once - find neo4j input below:")
            is_word_list_valid = False
            for line in neo4j_graph_input:
                print(line)

        return is_word_list_valid

    def check(self, validate, message):
        if validate():
            print("[+] {}".format(message))
            return True
        else:
            print("[-] {}".format(message))
            return False

    def is_file_name_valid(self):
        FILE_NAME_PATTERN = r"^(\w+)-([0-9abcdef]{8}\b)(-\w+)?(-\w+)?"

        expected_file_hash = list(self.word_list.file_hash_info.keys())[0]
        file_name = list(self.word_list.file_hash_info.values())[0]

        if len(file_name) > WordListValidator.FILE_NAME_MAX_LENGTH:
            return False

        result = re.match(FILE_NAME_PATTERN, file_name)
        if result is None:
            return False

        if result.group(self.FILE_NAME_NUMBER_OF_SEGMENTS_MAX + 1) is not None:
            return False

        file_hash = result.group(2)
        if file_hash is None:
            return False

        if file_hash != expected_file_hash:
            return False

        return True

    def is_character_set_valid(self):
        character_set = self.get_character_set()

        for word in self.word_list.word_list:
            for c in word:
                if c not in character_set:
                    return False
        return True

    def is_word_length_valid(self):
        for word in self.word_list.word_list:
            if len(word) < self.MIN_WORD_LENGTH or len(word) > self.MAX_WORD_LENGTH:
                return False
        return True

    def is_number_of_words_valid(self):
        if len(self.word_list.word_list) == self.NO_OF_WORDS:
            return True
        return False

    def is_list_of_words_sorted(self):
        word_list = self.word_list.word_list
        if word_list == sorted(word_list):
            return True
        return False

    def is_first_4_characters_unique(self):
        words_truncated = []
        for word in self.word_list.word_list:
            words_truncated.append(word[:4])

        if len(words_truncated) == len(set(words_truncated)):
            return True
        return False

    def get_neo4j_graph_with_levenshtein_distances(self):
        word_list = self.word_list.word_list

        nodes = []
        vertices = []

        for i in range(len(word_list)-1):
            word_a = word_list[i]
            for j in range(i+1, len(word_list)):
                word_b = word_list[j]
                word_a_mapped = self.map_word(word_a)
                word_b_mapped = self.map_word(word_b)
                d = distance(word_a_mapped, word_b_mapped)
                if d < self.MIN_LEVENSHTEIN_DISTANCE:
                    word_a_node = self.create_node_string(word_a)
                    word_b_node = self.create_node_string(word_b)
                    if word_a_node not in nodes:
                        nodes.append(word_a_node)
                    if word_b_node not in nodes:
                        nodes.append(word_b_node)
                    vertices.append(self.create_vertice_string(word_a, word_b))

        return nodes+vertices

    def get_character_set(self):
        character_set = []
        base_character_set = self.word_list.character_set[WordList.BASE_CHARACTER_SET]
        redundant_character_set = self.word_list.character_set[WordList.REDUNDANT_CHARACTER_SET]
        extra_character_set = self.word_list.character_set[WordList.EXTRA_CHARACTER_SET]

        if not extra_character_set:
            character_set = self.base_character_sets[base_character_set]
        else:
            character_set = self.base_character_sets[base_character_set] + [k for k in extra_character_set.keys()]

        for c in redundant_character_set:
            character_set.remove(c)

        return character_set

    def map_word(self, word):
        mappings = self.word_list.character_set[WordList.EXTRA_CHARACTER_SET]
        if not mappings:
            return word

        word_mapped = ""
        for c in word:
            if c in mappings.keys():
                word_mapped += mappings[c]
            else:
                word_mapped += c

        return word_mapped

    def create_node_string(self, word):
        part_1 = 'CREATE ({}:word'.format(word)
        part_2 = ' {value: '
        part_3 = '"{}"'.format(word)
        part_4 = '})'
        return part_1+part_2+part_3+part_4

    def create_vertice_string(self, word_a, word_b):
        part_1 = 'CREATE ({})'.format(word_a)
        part_2 = '-[:D]->({})'.format(word_b)
        return part_1+part_2

import hashlib
import os
import re
import sys
from scripts.src.WordList import WordList


class WordListReader:

    BASE_CHARACTER_SET_PATTERN = r"([a-z]+)"
    REDUNDANT_CHARACTER_SET_PATTERN = r"(-[a-z]+)?"
    EXTRA_CHARACTER_SET_PATTERN = r"((\+\w:\w)+)*"

    def parse_file(self, file_path):
        self.validate_file_exists(file_path)
        file_hash_info = self.get_file_hash_info(file_path)
        lines = self.read_file(file_path)
        base_character_set, redundant_character_set, extra_character_set = self.parse_first_line(lines[0])
        word_list = self.parse_word_list(lines)
        character_set = {
            WordList.BASE_CHARACTER_SET: base_character_set,
            WordList.REDUNDANT_CHARACTER_SET: redundant_character_set,
            WordList.EXTRA_CHARACTER_SET: extra_character_set
        }
        return WordList(character_set, word_list, file_hash_info)

    def validate_file_exists(self, file_path):
        if not os.path.isfile(file_path):
            print("File path {} does not exist. Exiting...".format(file_path))
            sys.exit()

    def get_file_hash_info(self, file_path):
        sha3_hash = hashlib.sha3_256()

        with open(file_path,"rb") as f:
            for bytes in iter(lambda: f.read(4096),b""):
                sha3_hash.update(bytes)
            file_name = os.path.basename(file_path)
            return {sha3_hash.hexdigest()[-8:]: file_name}

    def read_file(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
            return lines

    def parse_first_line(self, line):
        regex = r"^\[{}{}{}\]$".format(self.BASE_CHARACTER_SET_PATTERN,
                                       self.REDUNDANT_CHARACTER_SET_PATTERN,
                                       self.EXTRA_CHARACTER_SET_PATTERN)
        result = re.match(regex, line)
        if result is None:
            raise Exception("invalid first line syntax")

        character_set = result.group(1)
        if character_set is None:
            raise Exception("invalid first line syntax")

        redundant_characters_set = []
        if result.group(2) is not None:
            redundant_characters_set = list(result.group(2)[1:])

        mappings = {}
        if result.group(3) is not None:
            mappings_candidates = result.group(3).split('+')[1:]
            mappings = dict(zip([k[0] for k in mappings_candidates], [v[2] for v in mappings_candidates]))

        return character_set, redundant_characters_set, mappings

    def parse_word_list(self, lines):
        for line in lines:
            if line == "\n":
                raise Exception("empty lines not allowed")
            if not line.endswith("\n"):
                raise Exception("invalid line ending - the only one allowed is '\n'")
        return [line[:-1] for line in lines[1:]]

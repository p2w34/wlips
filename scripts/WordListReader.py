import os
import re
import sys
from scripts.WordList import WordList


class WordListReader:

    CHARACTER_SET_PATTERN = r"([a-z]+)"
    MAPPINGS_PATTERN = r"((\+\w:\w)+)*"

    def parse_file(self, file_path):
        self.validate_file_exists(file_path)
        lines = self.read_file(file_path)
        character_set, mappings = self.parse_first_line(lines[0])
        word_list = self.parse_word_list(lines)
        return WordList(character_set, mappings, word_list)

    def validate_file_exists(self, file_path):
        if not os.path.isfile(file_path):
            print("File path {} does not exist. Exiting...".format(file_path))
            sys.exit()

    def read_file(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
            return lines

    def parse_first_line(self, line):
        regex = r"^\[{}{}\]$".format(self.CHARACTER_SET_PATTERN, self.MAPPINGS_PATTERN)
        result = re.match(regex, line)
        if result is None:
            raise Exception("invalid first line syntax")

        character_set = result.group(1)
        if character_set is None:
            raise Exception("invalid first line syntax")

        if result.group(2) is None:
            return character_set, {}

        mappings_candidates = result.group(2).split('+')[1:]
        mappings = dict(zip([k[0] for k in mappings_candidates], [v[2] for v in mappings_candidates]))
        return character_set, mappings

    def parse_word_list(self, lines):
        for line in lines:
            if line == "\n":
                raise Exception("empty lines not allowed")
            if not line.endswith("\n"):
                raise Exception("invalid line ending - the only one allowed is '\n'")
        return [line[:-1] for line in lines[1:]]

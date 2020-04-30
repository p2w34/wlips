import hashlib
import os
import sys
from scripts.src.CharacterSetDescription import CharacterSetDescription
from scripts.src.WordList import WordList


class WordListReader:

    def parse_file(self, file_path):
        self.validate_file_exists(file_path)
        file_hash_info = self.get_file_hash_info(file_path)
        lines = self.read_file(file_path)
        character_set_description = CharacterSetDescription(lines[0])
        word_list = self.parse_word_list(lines)
        return WordList(character_set_description, word_list, file_hash_info)

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

    def parse_word_list(self, lines):
        for line in lines:
            if line == "\n":
                raise Exception("empty lines not allowed")
            if not line.endswith("\n"):
                raise Exception("invalid line ending - the only one allowed is '\n'")
        return [line[:-1] for line in lines[1:]]

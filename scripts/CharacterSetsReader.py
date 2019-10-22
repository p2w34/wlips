# This Python file uses the following encoding: utf-8
import os


class CharacterSetsReader:

    def parse(self, directory_path):
        character_sets = self.parse_character_sets(directory_path)
        return character_sets

    def parse_character_sets(self, directory_path):
        character_sets = {}
        for r, d, f in os.walk(directory_path):
            for file in f:
                characters = [ch for ch in open(os.path.join(r, file)).read() if ch != '\n']
                character_sets.update({file : characters})

        return character_sets

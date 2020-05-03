import argparse
import sys

from scripts.src.BaseCharacterSetsReader import CharacterSetsReader
from scripts.src.WordListCreator import WordListCreator

parser = argparse.ArgumentParser(
    description="Create word list based on the preliminary word list",
    epilog="Example: python3 scripts/create_word_list.py -l language")
parser.add_argument('-l', '--language', required=True)

args = parser.parse_args()
preliminary_word_list_path = "../wlip-0003/preliminary-word-lists/" + args.language

base_character_sets = CharacterSetsReader().parse("../wlip-0001/base-character-sets/")
word_list_creator = WordListCreator()
try:
    word_list = word_list_creator.create_word_list(preliminary_word_list_path, base_character_sets)
except:
    print("error: unable to parse word list file: '{}'".format(preliminary_word_list_path))
    sys.exit(1)

print("Created word list:\n")
print(word_list.word_list)

with open("../wlip-0003/word-lists/" + args.language + "-" + word_list.file_hash_info, "w") as f:
    f.write("[english]" + '\n')
    for word in word_list.word_list:
        f.write(word + '\n')

sys.exit(0)

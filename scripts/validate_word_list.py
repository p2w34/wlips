import argparse
import sys

from scripts.src.WordListReader import WordListReader
from scripts.src.WordListValidator import WordListValidator
from scripts.src.CharacterSetsReader import CharacterSetsReader

CHARACTER_SETS_PATH = "../wlip-0001/character-sets/"

parser = argparse.ArgumentParser(
    description="Validate word list",
    epilog="Example: python3 scripts/validate_word_list.py -f wlip-0003/english-770d1896-obsolete")
parser.add_argument('-f', '--file', required=True)

args = parser.parse_args()
file_name = args.file

base_character_sets = CharacterSetsReader().parse(CHARACTER_SETS_PATH)
word_list_reader = WordListReader()
try:
    word_list = word_list_reader.parse_file(file_name)
except:
    print("error: unable to parse word list file: '{}'".format(file_name))
    sys.exit(1)

is_valid_word_list = WordListValidator(base_character_sets, word_list).validate()

if not is_valid_word_list:
    print()
    print("error: word list in file: '{}' is invalid".format(file_name))
    sys.exit(1)

print("success: word list in file: '{}' is valid".format(file_name))
sys.exit(0)

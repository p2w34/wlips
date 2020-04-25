import argparse
from scripts.src.FileHash import FileHash

parser = argparse.ArgumentParser(
    description="Calculate SHA-3 hash of a file in hex form and outputs least significant 8 characters.",
    epilog="Example: python3 scripts/compute_file_hash.py -f wlip-0003/english-770d1896-obsolete")
parser.add_argument('-f', '--file', required=True)

args = parser.parse_args()
filename = args.file
file_hash = FileHash().compute_file_hash(filename)
print(file_hash)

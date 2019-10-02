import argparse
import hashlib

parser = argparse.ArgumentParser(
    description="Calculate SHA-3 hash of a file in hex form and outputs least significant 8 characters.",
    epilog="Example: python3 scripts/file_hash.py -f wlip-0003/english-770d1896-obsolete")
parser.add_argument('-f', '--file', required=True)

args = parser.parse_args()
filename = args.file

sha3_hash = hashlib.sha3_256()
with open(filename,"rb") as f:
    for bytes in iter(lambda: f.read(4096),b""):
        sha3_hash.update(bytes)
    print(sha3_hash.hexdigest()[-8:])

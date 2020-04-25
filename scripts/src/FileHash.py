import hashlib

class FileHash:

    def compute_file_hash(self, filename):
        sha3_hash = hashlib.sha3_256()
        with open(filename,"rb") as f:
            for bytes in iter(lambda: f.read(4096),b""):
                sha3_hash.update(bytes)
            return sha3_hash.hexdigest()[-8:]

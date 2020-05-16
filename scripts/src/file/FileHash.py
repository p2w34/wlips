import hashlib

class FileHash:

    def compute_file_hash(self, filename):
        sha3_hash = hashlib.sha3_256()
        with open(filename,"rb") as f:
            for bytes in iter(lambda: f.read(4096),b""):
                sha3_hash.update(bytes)
            return sha3_hash.hexdigest()[-8:]

    def compute_hash(self, character_set_description, list_of_words):
        all_file_lines = [character_set_description + '\n']
        all_file_lines = all_file_lines + [word + '\n' for word in list_of_words]

        sha3_hash = hashlib.sha3_256()
        for line in all_file_lines:
            sha3_hash.update(line.encode('utf-8'))
        return sha3_hash.hexdigest()[-8:]

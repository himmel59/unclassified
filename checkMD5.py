import hashlib
import os


def generate_hash(filepath: str, method: str, chunk_size: int = 1024):
    if not os.path.exists(filepath):
        raise Exception("The path does not exist")
    if not os.path.isfile(filepath):
        raise Exception("The path does not a file")

    if method == 'md5':
        hash = hashlib.md5()
    elif method == 'sha1':
        hash = hashlib.sha1()
    elif method == 'sha256':
        hash = hashlib.sha256()
    else:
        raise Exception("The method is not supported currently")

    with open(filepath, 'rb') as f:
        chunk = f.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)
    return hash.hexdigest()

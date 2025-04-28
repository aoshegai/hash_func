import hashlib

def hash_func(data: bytes) -> bytes:
    hash_object = hashlib.sha256()
    hash_object.update(data)
    return hash_object.digest()

if __name__ == "__main__":
    input_data = b"Hello world"
    hash_result = hash_func(input_data)
    print("Hash:", hash_result.hex())
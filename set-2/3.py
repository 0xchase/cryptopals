from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import random

def random_key(length):
    return get_random_bytes(length)

def encryption_oracle(data):
    before_size = random.randint(5, 10)
    before = random_key(before_size)

    after_size = random.randint(5, 10)
    after = random_key(after_size)

    key = random_key(16)

    if random.randint(0, 1) == 0:
        aes = AES.new(key, AES.MODE_ECB)
        ciphertext = aes.encrypt(data)
        return before + ciphertext + after
    else:
        iv = random_key(16)
        aes = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = aes.encrypt(data)
        return before + ciphertext + after

def detect_mode(data):
    for offset in range(0, len(data) % 16):
        blocks = [data[i:i+16] for i in range(offset, len(data), 16)]
        unique_blocks = set(blocks)

        if len(unique_blocks) < len(blocks):
            print("Detected ECB")
            return

    print("Detected CBC")

for i in range(64):
    data = b'A' * 64
    ciphertext = encryption_oracle(data)
    mode = detect_mode(ciphertext)
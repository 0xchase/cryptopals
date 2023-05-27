import base64
from Crypto.Cipher import AES

def xor(data, key):
    result = b''
    for i in range(len(data)):
        result += bytes([data[i] ^ key[i % len(key)]])
    return result

def cbc_encrypt(data, key, iv):
    aes = AES.new(key, AES.MODE_ECB)
    result = b''

    for i in range(0, len(data), AES.block_size):
        block = data[i:i+16]
        block = xor(block, iv)
        ciphertext = aes.encrypt(block)
        iv = ciphertext
        result += ciphertext

    return result

def cbc_decrypt(data, key, iv):
    aes = AES.new(key, AES.MODE_ECB)
    result = b''

    for i in range(0, len(data), AES.block_size):
        block = data[i:i+16]
        decrypted_block = aes.decrypt(block)
        plaintext_block = xor(decrypted_block, iv)
        iv = block
        result += plaintext_block

    return result

with open("2.txt", "r") as f:
    key = "YELLOW SUBMARINE".encode("utf-8")
    data = f.read().replace("\n", "")
    data = base64.b64decode(data)
    iv = b'\x00' * 16 # 128 bits

    decrypted = cbc_decrypt(data, key, iv)
    plaintext = base64.b64encode(decrypted)

    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted2 = aes.decrypt(data)
    plaintext2 = base64.b64encode(decrypted2)

    if plaintext == plaintext2:
        print("Decrypted successfully!")
        print(plaintext.decode("utf-8"))
    else:
        print("Decryption failed!")
import base64

def pad(data, length):
    padding_size = length % len(data)
    padding = (padding_size * chr(padding_size)).encode("utf-8")
    return data + padding

key = "YELLOW SUBMARINE".encode("utf-8")

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

data = b'\x00' * 16

with open("2.txt", "r") as f:
    d = f.read().replace("\n", "")
    b = base64.b64decode(d)

    iv = b'\x00' * 16 # 128 bits

    i = 0
    while i < len(b):
        block = b[i:i+16]
        data += xor(block, iv)
        print(data)
        i += 16
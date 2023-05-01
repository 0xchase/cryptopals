# Implement repeating-key XOR

from itertools import cycle

v = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""".encode('utf-8')

k = "ICE".encode('utf-8')

def xor(s, k):
    return (bytearray().join((a ^ b).to_bytes(1) for a, b in zip(s, cycle(k)))).hex()

print(xor(v, k))

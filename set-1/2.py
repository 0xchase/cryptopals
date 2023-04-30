# Write a function that takes two equal-length buffers and produces their XOR combination

def xor(a, b):
	a = bytes.fromhex(a)
	b = bytes.fromhex(b)
	c = bytearray(b'')
	for i in range(0, len(a)):
		c.append(a[i] ^ b[i])

	print(c.hex())

xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
		

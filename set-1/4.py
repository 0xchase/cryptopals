# Single byte XOR cipher

def decode(s):
	m = {}

	for c in s:
		if c in m.keys():
			m[c] += 1
		else:
			m[c] = 1

	key = ''
	count = 0

	for k in m.keys():
		if m[k] > count:
			count = m[k]
			key = k

	b = bytearray()
	for c in s:
		b.append(c ^ key)
	
	return b.decode()

a = open("4.txt", "r").read().split("\n")

for s in a:
	s = bytes.fromhex(s)

	try:
		print(decode(s))
	except:
		pass


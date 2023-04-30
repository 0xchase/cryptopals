# Single byte XOR cipher

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s = bytes.fromhex(s)

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

for c in s:
	print(chr(c ^ key), end='')
print("")
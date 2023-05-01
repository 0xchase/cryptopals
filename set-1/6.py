import base64

def hamming_distance(str1, str2):
    b1 = bytes(str1, 'utf-8')
    b2 = bytes(str2, 'utf-8')
    count = 0

    for i in range(len(b1)):
        if b1[i] & 0b1000 != b2[i] & 0b1000:
            count += 1
        if b1[i] & 0b0100 != b2[i] & 0b0100:
            count += 1
        if b1[i] & 0b0010 != b2[i] & 0b0010:
            count += 1
        if b1[i] & 0b0001 != b2[i] & 0b0001:
            count += 1

    return count

for key_size in range(2, 40):
    pass

with open("6.txt", "r") as f:
    data = f.read()
    data = base64.b64decode(data)

d = hamming_distance("this is a test", "wokka wokka!!!")
print(str(d))
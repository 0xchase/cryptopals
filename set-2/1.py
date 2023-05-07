def pad(data, length):
    padding_size = length % len(data)
    padding = (padding_size * chr(padding_size)).encode("utf-8")
    return data + padding

data = "YELLOW SUBMARINE".encode("utf-8")
data = pad(data, 20)
print(data)
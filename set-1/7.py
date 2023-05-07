from Crypto.Cipher import AES
import base64

key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)

with open("7.txt", "r") as f:
    data = f.read()
    data = base64.b64decode(data)
    data = cipher.decrypt(data)
    print(data.decode("utf-8"))

# Convert hex to base64

import sys
import base64

a = sys.argv[1]
b = bytes.fromhex(a)
e = base64.b64encode(b)
d = e.decode()

print(d)

with open("8.txt", "r") as f:
    data = f.read().split("\n")
    for line in data:
        i = 0
        while i < len(line):
            chunk1 = line[i:i+16]
            j = 0
            while j < len(line):
                chunk2 = line[j:j+16]
                if chunk1 == chunk2 and i != j:
                    print("ECB detected")
                    print(line)
                    break
                j += 16
            i += 16
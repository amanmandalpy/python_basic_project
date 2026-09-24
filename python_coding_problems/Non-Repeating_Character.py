test = "swiss"


counts = {}

for char in test:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

for char in test:
    if counts[char] == 1:
        print(char)
        break
from collections import defaultdict
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
message = ""

for i in range(8):
    letters = defaultdict(int)
    for line in lines:
        letters[line[i]] += 1
    message += min(letters, key=letters.get)

print(message)

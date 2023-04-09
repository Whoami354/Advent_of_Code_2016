lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
message = ""

for line in lines:
    letters = {}
    for letter in line:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    print(max(letters))


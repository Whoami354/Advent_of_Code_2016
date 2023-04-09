lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
sumRealRooms = 0

for line in lines:
    letters = {}
    checkLastLetters = ""
    words = line.split('-')
    lastValues = words[-1]
    words.pop()
    for word in words:
        for letter in word:
            if not letter in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        sortedLetters = sorted(letters.items(), key=lambda x:(-x[1],x[0]))[:5]
        checkTheLetters = [b[0] for b in sortedLetters]
        values = lastValues.split('[')
        roomID = int(values[0])
        commonLetters = values[1][:-1]
    for i in checkTheLetters:
        checkLastLetters += i
    checkLastLetters = checkLastLetters[:5]
    print(checkLastLetters)
    if checkLastLetters == commonLetters:
        sumRealRooms += roomID
print(sumRealRooms)
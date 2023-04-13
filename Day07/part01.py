import re

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
count = 0

for line in lines:
    wordsInBrackets = []
    wordsInNoBrackets = []
    inBracket = False
    for character in line:
        if character == '[':
            inBracket = True
            wordsInBrackets.append('')
        elif character == ']':
            inBracket = False
            wordsInNoBrackets.append('')
        elif inBracket:
            wordsInBrackets[-1] += character
        else:
            if len(wordsInNoBrackets) == 0:
                wordsInNoBrackets.append('')
            wordsInNoBrackets[-1] += character
    ispatternInBrackets = False
    ispatternOutBrackets = False
    for word in wordsInBrackets:
        if re.findall(r'([a-zA-Z])(?!\1)([a-zA-Z])\2\1', word):
            ispatternInBrackets = True
    for word in wordsInNoBrackets:
        if re.findall(r'([a-zA-Z])(?!\1)([a-zA-Z])\2\1', word):
            ispatternOutBrackets = True
    if ispatternOutBrackets and not ispatternInBrackets:
        count += 1
print(count)

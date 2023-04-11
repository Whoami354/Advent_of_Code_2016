import re
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

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
    patternInBrackets = False
    patternOutBrackets = False
    for word in wordsInBrackets:
        if re.findall("\b([a-zA-Z])(?!\1)([a-zA-Z])\2\1\b", word):
            patternInBrackets = True
    for word in wordsInNoBrackets:
        if re.findall("\b([a-zA-Z])(?!\1)([a-zA-Z])\2\1\b", word):
            patternOutBrackets = True
    print(patternInBrackets, patternOutBrackets)

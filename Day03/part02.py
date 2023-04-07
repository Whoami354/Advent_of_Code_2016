from itertools import chain

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
countTriangles = 0
horizontal = [[int(value) for value in row.split()] for row in lines]
vertical = list(chain.from_iterable(zip(*horizontal)))


for i in range(0, len(vertical), 3):
    firstSide = int(vertical[i])
    secondSide = int(vertical[i + 1])
    thirdSide = int(vertical[i + 2])
    checkSides1 = firstSide + secondSide
    checkSides2 = secondSide + thirdSide
    checkSides3 = thirdSide + firstSide
    if checkSides1 > thirdSide and checkSides2 > firstSide and checkSides3 > secondSide:
        countTriangles += 1

print(countTriangles)
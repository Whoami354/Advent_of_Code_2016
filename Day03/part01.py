lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
countTriangles = 0

for values in lines:
    sides = values.split()
    firstSide = int(sides[0])
    secondSide = int(sides[1])
    thirdSide = int(sides[2])
    checkSides1 = firstSide + secondSide
    checkSides2 = secondSide + thirdSide
    checkSides3 = thirdSide + firstSide
    if checkSides1 > thirdSide and checkSides2 > firstSide and checkSides3 > secondSide:
        countTriangles += 1
print(countTriangles)
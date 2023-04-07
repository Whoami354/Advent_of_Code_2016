lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

#lines = ["ULL", "RRDDD", "LURDL", "UUUUD"]


firstRow = [1, 2, 3]
secondRow = [4, 5, 6]
thirdRow = [7, 8, 9]
numbers = [firstRow, secondRow, thirdRow]
x,y = 1,1
combination = ""

for moves in lines:
    for move in moves:
        if move == 'U' and y > 0:
            y -= 1
        elif move == 'D' and y < 2:
            y += 1
        elif move == 'L' and x > 0:
            x -= 1
        elif move == 'R' and x < 2:
            x += 1
    combination += str(numbers[y][x])

print(combination)

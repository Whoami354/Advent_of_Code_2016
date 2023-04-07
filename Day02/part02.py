lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
#lines = ["ULL", "RRDDD", "LURDL", "UUUUD"]

firstRow = ['', '', '1', '', '']
secondRow = ['', '2', '3', '4', '']
thirdRow = ['5', '6', '7', '8', '9']
fourthRow = ['', 'A', 'B', 'C', '']
fifthRow = ['', '', 'D', '', '']
numbers = [firstRow, secondRow, thirdRow, fourthRow, fifthRow]
x, y = 0, 2
combination = ""

for moves in lines:
    for move in moves:
        if move == 'U' and y > 0 and numbers[y - 1][x] != '':
            y -= 1
        elif move == 'D' and y < 4 and numbers[y + 1][x] != '':
            y += 1
        elif move == 'L' and x > 0 and numbers[y][x - 1] != '':
            x -= 1
        elif move == 'R' and x < 4 and numbers[y][x + 1] != '':
            x += 1

    combination += str(numbers[y][x])

print(combination)

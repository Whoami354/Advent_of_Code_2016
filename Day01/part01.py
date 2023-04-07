lines = open("input", "r", encoding='utf-8').read().strip().split(', ')
directions = [0, 0, 0, 0]
direction = 0

for i in lines:
    letter = i[0]
    number = int(i[1:])
    if letter == 'L':
        direction -= 1
    else:
        assert letter == 'R'
        direction += 1
    direction %= len(directions)
    directions[direction] += number

print(abs(directions[0] - directions[2]) + abs(directions[1] - directions[3]))

import hashlib
input = "bwnlcvfs"

#1. pos = oben
#2. pos = unten
#3. pos = links
#4. pos = rechts


openDoor = ['b', 'c', 'd', 'e', 'f']
result = hashlib.md5(input.encode()).hexdigest()
print(result)
grid = [[' ' for _ in range(4)] for _ in range(4)]
grid[0][0] = 'S'
grid[3][3] = 'V'
isTarget = 'V'
newWay = input
possibilties = {}
ways = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}

def check_S_Coordinate(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 'S':
                return y,x

def moving_S(letter, grid):
    y,x = check_S_Coordinate(grid)
    grid[y][x] = ' '
    if letter == 'U':
        y -= 1
    if letter == 'D':
        y += 1
    if letter == 'L':
        x += 1
    if letter == 'R':
        x -= 1
    grid[y][x] = 'S'
    return grid

def setWalls(x: int, y: int, result):
    # 0: 'U', 1: 'D', 2: 'L', 3: 'R'
    if x == 0:
        result = '#' + result[1:]
    if x == 3:
        result = result[:2] + '#' + result[3:]
    if y == 0:
        result = result[0] + '#' + result[2:]
    if y == 3:
        result = result[:1] + '#' + result[3:]
    return result

while True:
    y,x = check_S_Coordinate(grid)
    print("Before", result)
    newResult = setWalls(x,y,result)
    print("After", result)

    while not grid[3][3] == 'S':
        y, x = check_S_Coordinate(grid)
        newResult = setWalls(x, y, result)

        for i in range(4):
            if newResult[i] in openDoor:
                newWay += (ways[i])
                grid = moving_S(ways[i], grid)
            # Das ziel wurde gefunden ? Überprüfen, ob der weg bereits gefunden wurde

        result = hashlib.md5(newWay.encode()).hexdigest()







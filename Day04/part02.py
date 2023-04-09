import string

lines = open("input", "r", encoding='utf-8').read().strip().split('\n')
sumRealRooms = 0

def cesarCipher(roomName: string, moves: int)-> string:
    roomName2 = ""
    for symbol in roomName:
        if symbol.isalpha():
            roomName2 += chr((ord(symbol) + moves - 97) % 26 + 97)
        else:
            roomName2 += symbol
    return roomName2

for line in lines:
    roomName1 = ""
    words = line.split('-')
    lastValues = words[-1]
    sectorID = int(lastValues.split('[')[0])
    words.pop()
    for letters in words:
        roomName1 += cesarCipher(letters, sectorID)
    if "northpole" in roomName1:
        print(sectorID)


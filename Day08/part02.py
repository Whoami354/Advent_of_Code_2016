import numpy as np
import re
lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

class Screen:
    def __init__(self):
        self.width = 50
        self.height = 6
        self.pixels = np.full((self.height, self.width), '.')
    def __repr__(self):
        return str(self.pixels)

    def createRectangle(self, width: int, height: int):
        for y in range(height):
            for x in range(width):
                self.pixels[y][x] = '#'

    def moveColumn(self, x: int, moves: int):
        for i in range(moves):
            tmp = self.pixels[-1][x]
            for y in reversed(range(self.height)):
                self.pixels[y][x] = self.pixels[y - 1][x]
            self.pixels[0][x] = tmp

    def moveRow(self, y: int, moves: int):
        for i in range(moves):
            tmp = self.pixels[y][-1]
            for x in reversed(range(self.width)):
                self.pixels[y][x] = self.pixels[y][x - 1]
            self.pixels[y][0] = tmp

if __name__ == '__main__':
    screen = Screen()
    for line in lines:
        if line.startswith('rect'):
            width, height = re.findall(r'\d+', line)
            screen.createRectangle(int(width), int(height))
        elif line.startswith('rotate column'):
            x, moves = re.findall(r'\d+', line)
            screen.moveColumn(int(x), int(moves))
        elif line.startswith('rotate row'):
            y, moves = re.findall(r'\d+', line)
            screen.moveRow(int(y), int(moves))
    for i in range(0, 50, 5):
        print(screen.pixels[:, i:i + 5])

    #RURUCEOEIL
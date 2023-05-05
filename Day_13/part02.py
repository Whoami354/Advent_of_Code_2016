import math
import sys
from collections import deque
from functools import lru_cache, partial

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

favorite_number = 1358
target = (31, 39)


@lru_cache
def isWall(x: int, y: int):
    binaryNumber = bin((x * x + 3 * x + 2 * x * y + y + y * y) + favorite_number)
    return binaryNumber.count("1") % 2 == 1


path_cache = set()


def calc_image(path=[], window_size=(50, 50)):
    for elem in path:
        path_cache.add(elem)
    a = np.zeros(window_size)
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            a[x, y] = isWall(x, y)
    try:
        for x, y in path_cache:
            a[x, y] = 1.8
    except:
        pass
    a[target] = 2.5
    try:
        for x, y in path:
            a[x, y] = 2
    except IndexError:
        pass
    return a.T


def animate(i, path_gen):
    try:
        path = next(path_gen)
    except:
        return
        sys.exit()

    image_plot.set_data(calc_image(path))
    return image_plot


fig = plt.figure()
image_plot = plt.imshow(calc_image())


def BFS():
    def can_explore(x: int, y: int):
        return not (x < 0 or y < 0 or isWall(x, y))

    start = (1, 1)
    visited = set()
    queue = deque([(*start, [])])
    while queue:
        x, y, path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        new_path = path.copy()
        new_path.append((x, y))
        yield new_path

        if can_explore(x - 1, y):
            queue.append((x - 1, y, new_path))
        if can_explore(x + 1, y):
            queue.append((x + 1, y, new_path))
        if can_explore(x, y - 1):
            queue.append((x, y - 1, new_path))
        if can_explore(x, y + 1):
            queue.append((x, y + 1, new_path))

        if len(path) > 50:
            print("Länge von Path", len(visited) - 1)
            break

if __name__ == "__main__":
    path_gen = BFS()
    anim = animation.FuncAnimation(
        fig,
        func=partial(animate, path_gen=path_gen),
        frames=None,
        interval=1,
        repeat=False,
    )
    plt.show()

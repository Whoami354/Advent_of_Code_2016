from functools import lru_cache
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from functools import partial
from collections import deque
from sortedcontainers.sortedset import SortedSet
from collections import defaultdict
import math
import sys

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

        if target == (x,y):
            print("Länge von Path", len(path))
            break
@lru_cache
def optimal_distance(x, y):
    """
    returns the underestimation of the path to the target node
    """
    return abs(x - target[0]) + abs(y - target[1])

def A_STAR():
    def recreate_path(current, previous_dict):
        path = []
        while previous_dict[current]:
            path = [current] + path
            current = previous_dict[current]
        return path

    def can_explore(x, y):
        if x < 0 or y < 0:
            return False
        if isWall(x, y):
            return False
        return True

    start = (1, 1)
    visited = set()
    cost_dict = defaultdict(lambda: math.inf)
    cost_dict[start] = 0
    previous_dict = {start: None}
    to_explore = SortedSet([start], lambda x: cost_dict[x] + optimal_distance(*x))

    while to_explore:
        current = to_explore.pop(0)
        x, y = current
        if x == target[0] and y == target[1]:
            print("fin:", len(recreate_path(current, previous_dict)))
            return

        if current in visited:
            continue

        visited.add(current)

        path = recreate_path(current, previous_dict)
        yield path

        def handle_neighbour(x, y, current):
            if can_explore(x, y) and cost_dict[(x, y)] > cost_dict[current] + 1:
                cost_dict[(x, y)] = cost_dict[current] + 1
                previous_dict[(x, y)] = current
                to_explore.add((x, y))

        handle_neighbour(x - 1, y, current)
        handle_neighbour(x + 1, y, current)
        handle_neighbour(x, y - 1, current)
        handle_neighbour(x, y + 1, current)
    print("queue empty", to_explore)

if __name__ == "__main__":
    path_gen = A_STAR()
    anim = animation.FuncAnimation(
        fig,
        func=partial(animate, path_gen=path_gen),
        frames=None,
        interval=1,
        repeat=False,
    )
    plt.show()

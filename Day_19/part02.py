import numpy as np

INPUT = 3018458

def new_rules(elves):
    n = len(elves)
    if n <= 2:
        return elves[0] + 1

    across = n // 2
    if n % 2:
        removed = n - (n+1)//3
        new = np.roll(elves, -across)[1::3]
    else:
        removed = n - n//3
        new = np.roll(elves, -across)[2::3]

    return new_rules(np.roll(new, across-removed))


elf_circle = np.arange(INPUT)

print(f"Who is the winner now? Elf {new_rules(elf_circle)}?")
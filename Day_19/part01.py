import numpy as np

INPUT = 3018458

def find_elf(elves):
    if len(elves) <= 2:
        return elves[0] + 1

    if len(elves) % 2:
        return find_elf(np.roll(elves[::2], 1))
    else:
        return find_elf(elves[::2])



elf_circle = np.arange(INPUT)

print("Hey Elves, why don't you start playing the Yankee swap?")
print(f"Who did win all presents? Elf {find_elf(elf_circle)}?")

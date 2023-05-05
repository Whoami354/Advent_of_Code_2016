lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

discs = []
positions = []
for line in lines:
    line = line.strip()
    position = int(line.split()[3])
    disc = int(line.split()[-1][:-1])
    positions.append(position)
    discs.append(disc)

print(positions)
print(discs)
print('---')

time = 0
while True:
    new = []
    for idx, x in enumerate(discs):
        value = (x + time + 1 + idx) % positions[idx]
        new.append(value)

    #print(new)
    if len(set(new)) == 1:
        break

    time += 1

print(time)



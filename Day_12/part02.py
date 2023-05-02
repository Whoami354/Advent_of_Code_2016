import re
commands = open("input", "r", encoding='utf-8').read().strip().split('\n')

registers = {x: 0 for x in ['a', 'b', 'c', 'd']}
registers['c'] = 1

command_idx = 0

while command_idx < len(commands):
    command = commands[command_idx]

    if command.startswith("inc"):
        registers[command[4]] += 1
    if command.startswith("dec"):
        registers[command[4]] -= 1
    if command.startswith("jnz"):
        condition, jumps = re.search(r'jnz (\w+) (\-?\w+)', command).groups()
        if condition.isnumeric(): condition = int(condition)
        else: condition = registers[condition]
        jumps = int(jumps)
        if condition != 0:
            command_idx += jumps
            continue
    if command.startswith("cpy"):
        value, target = re.search(r'cpy (\w+) ([a-z]+)', command).groups()
        if value.isnumeric(): value = int(value)
        else: value = registers[value]
        registers[target] = value

    command_idx += 1


print(registers)



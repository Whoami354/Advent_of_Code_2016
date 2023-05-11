lines = open("input", "r", encoding='utf-8').read().strip().split('\n')

blocked_ranges = []

for entry in lines:
    start, end = map(int, entry.split('-'))
    blocked_ranges.append((start, end))

blocked_ranges.sort()
lowest_ip = 0
for start, end in blocked_ranges:
    if lowest_ip < start:
        break
    lowest_ip = max(end + 1, lowest_ip)

if lowest_ip <= 4294967295:
    print(lowest_ip)


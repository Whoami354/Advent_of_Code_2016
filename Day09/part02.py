def decompress_count(input_str: str) -> int:
    try:
        marker_start = input_str.index('(')
        marker_end = input_str.index(')')
        before = input_str[:marker_start]
        marker = input_str[marker_start + 1: marker_end]
        after = input_str[marker_end + 1:]

        n_values, n_times = [int(val) for val in marker.split('x')]

        decompressed_count = len(before) + decompress_count(after[:n_values]) * n_times + decompress_count(after[n_values:])
    except ValueError:
        decompressed_count = len(input_str)
    return decompressed_count

def part2(data: str) -> int:
    return decompress_count(data)

def parse_input(filename: str):
    return open(filename).read().strip()

data = parse_input('input')
print(f'Part 2: {part2(data)}')
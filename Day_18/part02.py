input = ".^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^"
rows = [input]
countSafe = input.count('.')
num_rows = 400000

def isTrap(left,center,right):
    return (left == '^' and center == '^' and right == '.') or (left == '.' and center == '^' and right == '^') or (left == '^' and center == '.' and right == '.') or (left == '.' and center == '.' and right == '^')

for _ in range(num_rows - 1):
    prev_row = rows[-1]
    next_row = ''
    for i in range(len(prev_row)):
        left = prev_row[i - 1] if i > 0 else '.'
        center = prev_row[i]
        right = prev_row[i + 1] if i < len(prev_row) - 1 else '.'

        if isTrap(left,center,right):
            next_row += '^'
        else:
            next_row += '.'
    rows.append(next_row)
    countSafe += next_row.count('.')

print(countSafe)

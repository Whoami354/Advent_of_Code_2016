def isInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


reg = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

data = open('input').read().splitlines()
data = [x.split(' ') for x in data]

i = 0

while i < len(data):
    d = data[i]
    if d[0] == 'cpy':
        t = d[1]
        r = d[2]
        ### Optimization no. 1 ###
        if not isInt(t) and not isInt(r):
            d1 = data[i + 1]
            d2 = data[i + 2]
            d3 = data[i + 3]

            if d1[0] == 'dec' and d2[0] == 'inc' and d3[0] == 'jnz' and d3[2] == '-2':
                reg[d[1]] = reg[d[1]] * 2
                reg[d[2]] = 0
                i += 4
                continue
        ### End Optimization no. 1 ###
        if isInt(t) and isInt(r):
            i += 1
            continue
        if isInt(t):
            t = int(t)
        else:
            t = reg[t]
        reg[r] = t

    if d[0] == 'inc':
        ### Optimization no. 2 ###
        d1 = data[i + 1]
        d2 = data[i + 2]
        d3 = data[i + 3]
        d4 = data[i + 4]
        if d1[0] == 'dec' and d2[0] == 'jnz' and d2[2] == '-2' and d3[0] == 'dec' and d4[0] == 'jnz' and d4[2] == '-5':
            reg[d[1]] = reg[d[1]] + (reg[d1[1]] * reg[d3[1]])
            reg[d1[1]] = 0
            reg[d3[1]] = 0
            i += 5
            continue
        ### End Optimization no. 2 ###
        if d[1] in reg:
            reg[d[1]] = reg[d[1]] + 1

    if d[0] == 'dec':
        if d[1] in reg:
            reg[d[1]] = reg[d[1]] - 1

    if d[0] == 'tgl':
        oset = i + reg[d[1]]
        if oset > len(data) - 1:
            i += 1
            continue

        gt = data[oset]
        if len(gt) == 2:
            if gt[0] == 'inc':
                data[oset][0] = 'dec'
            else:
                data[oset][0] = 'inc'
        if len(gt) == 3:
            if gt[0] == 'jnz':
                data[oset][0] = 'cpy'
            else:
                data[oset][0] = 'jnz'
        i += 1
        continue

    if d[0] == 'jnz':
        t = d[1]
        r = d[2]
        if isInt(t):
            t = int(t)
        else:
            t = reg[t]
        if isInt(r):
            r = int(r)
        else:
            r = reg[r]
        if t != 0:
            i = i + r
        else:
            i += 1
    else:
        i += 1

print(reg)
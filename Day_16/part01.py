input = "00111101111101000"
disk_size = 272

def dragon_curve(data, size):
    while len(data) < size:
        a = data
        b = a[::-1].translate(str.maketrans("01", "10"))
        data = a + "0" + b
    return data[:size]

def checksum(data):
    while len(data) % 2 == 0:
        data = ''.join(['1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2)])
    return data

data = dragon_cuve(input, disk_size)
checksum_data = checksum(data)
print(checksum_data)
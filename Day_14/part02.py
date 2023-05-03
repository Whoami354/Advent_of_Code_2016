import re
import hashlib
hashes = []
input_hashing = "cuanljph"

def calculateHash(input, number):
    if number >= len(hashes):
        salt_decimal = input + str(number)
        hash = hashlib.md5(salt_decimal.encode()).hexdigest()
        for i in range(2016):
            hash = hashlib.md5(hash.encode()).hexdigest()
        hashes.append(hash)
    return hashes[number]

found = 0
idx = 0

while found < 64:
    hash1 = calculateHash(input_hashing, idx)
    m = re.search(r"(\w)\1\1", hash1)
    if m != None:
        m = m.group(1)
        for i in range(idx + 1, idx + 1000):
            hash2 = calculateHash(input_hashing, i)
            n = re.search(m * 5, hash2)
            if n != None:
                found += 1
                break
    idx += 1

print(idx - 1)
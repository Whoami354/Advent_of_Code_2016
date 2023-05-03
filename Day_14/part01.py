import re
import hashlib
input = "cuanljph"

foundKeys = 0
idx = 0

def hashIdx(idx: int):
    salt_decimal = input + str(idx)
    md5_output = hashlib.md5(salt_decimal.encode()).hexdigest()
    return md5_output

while foundKeys < 64:
    idx += 1
    md5_output = hashIdx(idx)
    findThreeCharacters = re.search(r"(\w)\1\1", md5_output)
    if not findThreeCharacters:
        continue
    findThreeCharacters = findThreeCharacters.group(1)
    for i in range(1, 1001):
        new_Hash = hashIdx(idx + i)
        if re.search(findThreeCharacters * 5, new_Hash):
            foundKeys += 1
            if foundKeys == 64:
                print(idx)
                break




import hashlib
input = "uqwqemis"

hashValue = input
sumPasswd = ""
idx = 0

result = hashlib.md5(hashValue.encode('utf-8')).hexdigest()

while len(sumPasswd) < 8:
    hashValue = input + str(idx)
    result = hashlib.md5(hashValue.encode('utf-8')).hexdigest()
    if result.startswith("00000"):
        sumPasswd += result[5]
    idx += 1

stringIdx = str(idx)
print(sumPasswd)
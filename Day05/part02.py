import hashlib
input = "uqwqemis"

hashValue = input
password = [""] * 8
idx = 0

result = hashlib.md5(hashValue.encode('utf-8')).hexdigest()

while '' in password:
    hashValue = input + str(idx)
    result = hashlib.md5(hashValue.encode('utf-8')).hexdigest()
    if result.startswith("00000"):
        position = result[5]
        if position.isdigit():
            position = int(position)
            if position < 8 and password[position] == '':
                password[position] = result[6]
                print(password)

    idx += 1

stringPWD = ''.join(password)
print(stringPWD)


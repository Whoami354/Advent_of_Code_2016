import re
text = open("input", "r", encoding='utf-8').read().strip()

def decompressed(text: str) -> str:
    output = ""
    while text:
        result = re.search(r"\((\d+)x(\d+)\)", text)
        if not result:
            output += text
            return output
        deepLetters = int(result.group(1))
        repeat = int(result.group(2))

        output += text[:result.start()]
        text = text[result.end():]

        output += text[:deepLetters] * repeat
        text = text[deepLetters:]
    return output

print(len(decompressed(text)))

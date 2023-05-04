import re

def countBits(n):
    if n == 0:
        return 0
    x = bin(n)[2:]
    s = str(x)

    c = re.findall("1", s)

    return len(c)

result = countBits(10);
print(result)
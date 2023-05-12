
# Find the sum of all multiples of 3 and 5 below 1000. Like below 10 are: 3+5+6+9 = 23

import sys

def multiples(n):
    sum = 0
    for i in range(1,n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum = sum + i

    return sum

n = int(sys.argv[1])

print(multiples(n))

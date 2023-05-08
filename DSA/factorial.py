# using recursion process to solve the problem

import sys

def factorial(n):
    if n<1:
        return 1
    else:
       ans = n * factorial(n-1) # recursion starts here and will continue until n-1 -> less than 1
    
    return ans

if len(sys.argv) < 2:
    print("EMPTY! enter like this: python3 factorial.py <your number>")
else:

    n = sys.argv[1]
    print(factorial(int(n)))

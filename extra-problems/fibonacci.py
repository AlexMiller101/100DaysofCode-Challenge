# Python program to display the Fibonacci sequence by recursion

import sys

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

n = int(sys.argv[1])

if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci Series: ")
   print("")
   for i in range(n):
       if i == n:
           print(fibonacci(i))
           print("\n") 
       else:
          print(fibonacci(i), end=" ")
print("")
print("")

def isPalindrome(x):
    s = str(x)
    s = list(s)
    s.reverse()
    
    s = "".join(s)
    if int(s) == x:
        return True
    else:
        return False

x = int(input("Enter the Number: "))
print("Is {} a Palindrome Number? {}".format(x,isPalindrome(x)))
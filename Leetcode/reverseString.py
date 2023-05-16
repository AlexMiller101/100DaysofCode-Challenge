# Reverse a String given in a array form


def reverseString(s): # simplest solution
    s.reverse()

def twoPointerReverseString(s): # two pointer solution
    l, r = 0, len(s)-1

    while(l<r):
        temp = s[l]
        s[l] = s[r]
        s[r] = temp

        l += 1
        r -= 1    

s = ["h", "i"]
print("Input: {}".format(s))
twoPointerReverseString(s) 
print("Output: {}".format(s))
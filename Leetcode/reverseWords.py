
# Reversing words in a string

def reverseWords(s):
    n = s.split()
    for x, i in enumerate(n):
        n[x] = i[::-1] # [::-1] is used for reversing array

    return ' '.join(n)

s = "Let's take leetcode"
r_s = "s'teL ekat edocteel"

s = reverseWords(s)
print(s)
print(s==r_s )

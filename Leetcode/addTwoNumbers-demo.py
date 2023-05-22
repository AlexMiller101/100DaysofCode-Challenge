
def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()

    s1 = ''.join(str(x) for x in l1)
    s2 = ''.join(str(x) for x in l2)
    
    s1 = int(s1)
    s2 = int(s2)

    sum = s1 + s2

    s = list(str(sum))
    s.reverse()

    return s


l1 = [2,4,3]
l2 = [5,6,4]

print(addTwoNumbers(l1, l2))

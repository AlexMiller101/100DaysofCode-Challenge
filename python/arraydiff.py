
def array_diff(a, b):

    for i in a:
        for item in b:
            try:
                a.remove(item)
            except:
                continue

    return a; 

result = array_diff([1,2,2], [2])
print(result)
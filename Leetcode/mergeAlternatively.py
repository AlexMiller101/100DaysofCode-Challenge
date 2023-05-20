
# merge two strings letters alternatively

def mergeAlternatively(word1, word2):
    if len(word1) < len(word2):
        min = len(word1)
    else:
        min = len(word2)

    merged = ""

    for i in range(min):
        merged += word1[i]
        merged += word2[i]

    if len(word1) > len(word2):
        merged += word1[min:]
    else:
        merged += word2[min:]

    return merged        


word1 = "abc"
word2 = "pqrs"

print(mergeAlternatively(word1, word2))
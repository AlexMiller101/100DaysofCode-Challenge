length_object = {}

def findLength(nums, i):
    s1 = list(filter(lambda x: x==i, nums))
    #print(s1)
    
    length_object[len(s1)] = i

    return len(s1)

def topKFrequent(nums, k):
    if len(nums) <= 1:
        return nums

    s = set(nums)
    if len(s) <= 1 or len(s) == len(nums):
        return list(s)

    length_list = []
    print(s)

    for i in s: # loop to find length of each sub list of containing same item.
        l = findLength(nums, i) # calling the function for finding
        length_list.append(l)
    
    print(length_object)
    #print(length_list)
    length_list.sort(reverse=True) # sorting for ranking
    length_list = length_list[:k] # to restrict the ranking to k
    print(length_list)
    r = []

    for i in length_list:
        r.append(length_object[i])

    return r

nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))
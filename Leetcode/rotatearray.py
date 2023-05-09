def rotatearraybyone(nums):
    
    r = len(nums)-2 # one pointer is last second
    temp = nums[len(nums)-1] # already storing the first element in a temp file

    while(r>=0):
        nums[r+1] = nums[r] # changing the one step ahead r+1 pointer with r pointer and repeat till reaching 0
        r -= 1
    nums[0] = temp # at last, change the last element with the first element stored in temp

def rotatearray(nums, k):
    i = 1
    while(i<=k):
        rotatearraybyone(nums)
        i += 1
    return nums

def optimizedRotate(nums, k):
    k = k % (len(nums)) # since, rotating to the length of list makes it the same or cycle
    
    # reversing
    nums.reverse()
    #print(nums)

    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    #print(nums)

    # reverse the remaining elements

    nums[k:] = reversed(nums[k:])
    print(nums)

optimizedRotate([1,2,3,4,5],3)

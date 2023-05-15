
def containDuplicate(nums):
    nums.sort() # sort the numbers in ascending order

    l, r = 0, 1 # setting up two pointers

    while(r<len(nums)):
        if nums[l] == nums[r]:
            return True
        else:
            l += 1
            r += 1

    return False

def optimizedcontainDuplicate(nums): # this is using set
    return len(set(nums)) != len(nums)

nums = [1,2,3,1]

#print("Output: {}".format(containDuplicate(nums)))
print("Output: {}".format(optimizedcontainDuplicate(nums)))


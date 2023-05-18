
def removeDuplicate(nums):
    l, r = 0, 1

    while(r<len(nums)):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        r += 1
    return l+1

nums = [1,1,2]
print(removeDuplicate(nums))
print(nums)
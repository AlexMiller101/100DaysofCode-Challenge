def twoSum(nums, target):
    output = []
    for n in range(0,len(nums)):
        for i in range(0, len(nums)):
            sum = nums[n] + nums[i]
            if i == n:
                break
            if sum == target:
                output.append(i)
                output.append(n)

    return output

# example value for testing, it should give [1,2]
#out = twoSum([3,2,4], 6)
#print(out)

"""
Below is the improvised and optimized version of the solution
found in the leetcode solution page. It uses one loop
"""

def optimized_twosum(num, target):
    seen = {}

    for i in range(0, len(num)):
        diff = target - num[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[num[i]] = i


optimized_out = optimized_twosum([3,2,4], 6)
print(optimized_out)
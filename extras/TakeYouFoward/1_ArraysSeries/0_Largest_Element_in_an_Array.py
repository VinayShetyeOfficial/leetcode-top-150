# Largest Element in an Array

import random

# Find Largest Element in Array
def compute(nums: list[int]) -> int:
    print(nums)
    nums = set(nums)
    largestNum = next(iter(nums))
 
    for num in nums:
        if num > largestNum:
            lagestNum = num
            
    return largestNum

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    ans = compute(arr)
    print(ans)

#===================================================
# Error
class Solution:
    def largestElement(self, nums):
        nums = set(nums)
        largestNumber = nums[0]

        for num in nums:
            if num > largestNumber:        # TypeError: 'set' object is not subscriptable
                largestNumber = num

        return largestNumber
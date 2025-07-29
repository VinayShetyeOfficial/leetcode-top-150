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
#===================================================

import random

# Find Second-Largest/Second-Smallest Element in Array
def compute(nums: list[int]) -> None:
    smallest = second_smallest = float('inf')
    largest = second_largestt = float('-inf')
    
    for num in nums:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
            
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    print(second_smallest)
    print(second_largest)

if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(10)]
    ans = compute(arr)

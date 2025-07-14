# Largest Element in an Array

class Solution:
    def largestElement(self, nums):
        nums = set(nums)
        largestNumber = nums[0]

        for num in nums:
            if num > largestNumber:
                largestNumber = num

        return largestNumber
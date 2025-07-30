# Link: https://leetcode.com/problems/range-sum-query-immutable/description/

# Range Sum Query - Immutable
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)  
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
    
# ====================================================================

# Alternate Solution

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right+1])
        
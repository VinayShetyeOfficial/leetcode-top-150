# Link: https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List

# ============================================
# Solution 1: Using Prefix Sum (Optimal)
# ============================================
class NumArray1:
    def __init__(self, nums: List[int]):
        # Create prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)  
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Return sum from left to right using prefix sum
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

"""
Time Complexity:
- __init__: O(n) to build prefix sum
- sumRange: O(1)
Space Complexity: O(n) for prefix sum array
"""

# ============================================
# Solution 2: Direct Sum (Brute Force)
# ============================================
class NumArray2:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # Directly calculate sum of the subarray
        return sum(self.nums[left:right+1])

"""
Time Complexity:
- __init__: O(1)
- sumRange: O(n) where n = right - left + 1
Space Complexity: O(1)
"""

# ============================================
# Driver Code
# ============================================
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    # Using Solution 1
    obj1 = NumArray1(nums)
    print("Solution1 sumRange(0,2):", obj1.sumRange(0,2))
    print("Solution1 sumRange(1,3):", obj1.sumRange(1,3))

    # Using Solution 2
    obj2 = NumArray2(nums)
    print("Solution2 sumRange(0,2):", obj2.sumRange(0,2))
    print("Solution2 sumRange(1,3):", obj2.sumRange(1,3))

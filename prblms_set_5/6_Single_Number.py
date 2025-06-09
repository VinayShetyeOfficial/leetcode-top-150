# 136. Single Number (Easy)
# https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the single number using XOR.
        All duplicate numbers cancel out, leaving the unique one.
        """
        result = 0
        for num in nums:
            result ^= num
        return result

"""
✅ Time Complexity: O(n)
👉 One pass through the list

✅ Space Complexity: O(1)
👉 Only one variable used
"""
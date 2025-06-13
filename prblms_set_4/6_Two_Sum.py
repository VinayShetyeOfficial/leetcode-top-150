# 1. Two Sum (Easy) - Done
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of the two numbers such that they add up to target.
        Uses a hash map to track previously seen numbers for O(1) lookup.
        """
        seen = {}  # Stores number → index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            

"""
✅ Time Complexity: O(n)
👉 Each element is visited once

✅ Space Complexity: O(n)
👉 Hashmap stores up to n elements
"""
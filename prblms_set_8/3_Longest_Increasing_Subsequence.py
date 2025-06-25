# 300. Longest Increasing Subsequence (Medium) - Done
# https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)  # Every number alone is a subsequence of length 1

        # Start from end and move to start
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # We can include nums[i] before nums[j]
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


"""
✅ Time Complexity: O(n^2)
Two nested loops: one for each i, and one for each j > i

✅ Space Complexity: O(n)
For the LIS array
"""
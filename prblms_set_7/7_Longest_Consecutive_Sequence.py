# 128. Longest Consecutive Sequence (Medium) - Done
# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Only start counting if it's the start of a sequence
            if num - 1 not in numSet:
                current = num
                streak = 1

                while current + 1 in numSet:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest

"""
✅ Time: O(n)
- We visit each number once, and for each sequence, we only scan it once.

✅ Space: O(n)
- For the HashSet used to store unique numbers.
"""
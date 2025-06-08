# 28. Find the Index of the First Occurrence in a String (Easy)
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of needle in haystack,
        or -1 if needle is not part of haystack.
        """

        # Edge case: empty needle
        if not needle:
            return 0

        # Sliding window approach
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


"""
✅ Time Complexity: O((n - m + 1) * m)
👉 n = length of haystack, m = length of needle

✅ Space Complexity: O(1)
👉 No extra space used beyond a few variables
"""
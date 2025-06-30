# 392. Is Subsequence (Easy) - Done
# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Returns True if s is a subsequence of t, else False.
        """

        s_ptr, t_ptr = 0, 0

        # Traverse both strings
        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

        return s_ptr == len(s)


"""
✅ Time Complexity: O(n)
👉 n = length of t

✅ Space Complexity: O(1)
👉 Only two pointers used, no extra space
"""

# Alternate
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1

        return i == len(s)
        
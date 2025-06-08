# 58. Length of Last Word (Easy) - Done
# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word without using split().
        This is more space efficient.
        """
        i = len(s) - 1
        length = 0

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


"""
✅ Time Complexity: O(n)
👉 Where n is the number of characters in the string.

✅ Space Complexity: O(n)
👉 Due to space used by split() (can be optimized further).
"""
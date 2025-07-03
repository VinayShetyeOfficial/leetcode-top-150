# 3. Longest Substring Without Repeating Characters (Medium) - Done
# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.
        Uses sliding window and hash map to track last seen positions.
        """

        char_index = {}      # Dictionary to store last index of each character
        max_length = 0
        left = 0             # Left pointer of the window

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move left pointer to one position after the last occurrence
                left = char_index[s[right]] + 1

            char_index[s[right]] = right  # Update last seen index
            max_length = max(max_length, right - left + 1)

        return max_length

"""
✅ Time Complexity: O(n)
👉 Each character is visited at most twice.

✅ Space Complexity: O(min(n, m))
👉 Where n = length of string, m = size of character set (e.g., 26 for lowercase letters)
"""
# Alternate Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
"""
✅ Time Complexity: O(n)
👉 Each character is visited at most twice (once by right pointer, once by left)

✅ Space Complexity: O(n)
👉 Set stores up to n characters in the worst case (all unique)
"""
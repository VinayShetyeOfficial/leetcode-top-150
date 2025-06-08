# 14. Longest Common Prefix (Easy) - Done
# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Returns the longest common prefix among all strings in the list.
        """

        if not strs:
            return ""

        # Loop through characters in the first string
        for i in range(len(strs[0])):
            current_char = strs[0][i]

            # Compare current character with same position in all other strings
            for word in strs[1:]:
                # If index is out of bounds or characters don't match
                if i >= len(word) or word[i] != current_char:
                    return strs[0][:i]

        # Entire first string is a prefix
        return strs[0]

"""
✅ Time Complexity: O(n * m)
👉 Where n = number of strings, m = length of the shortest string

✅ Space Complexity: O(1)
👉 No extra space used beyond a few variables
"""

# 205. Isomorphic Strings (Easy)
# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Returns True if s and t are isomorphic.
        Each character must map to one and only one character in the other string.
        """

        # Create two maps: s → t and t → s
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            # If mapping exists, verify it's consistent
            if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or \
               (char_t in map_t_to_s and map_t_to_s[char_t] != char_s):
                return False

            # Otherwise, set the mapping
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True


"""
✅ Time Complexity: O(n)
👉 Where n = length of strings

✅ Space Complexity: O(1)
👉 Only 2 dictionaries used (at most 26 characters for lowercase letters)

"""


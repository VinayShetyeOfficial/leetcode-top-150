# 383. Ransom Note (Easy) - Done
# https://leetcode.com/problems/ransom-note

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Returns True if ransomNote can be constructed from magazine.
        Each letter can be used only once.
        """

        # Count frequency of each letter in both strings
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if magazine has enough of each character
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False

        return True


"""
✅ Time Complexity: O(n + m)
👉 Where n = len(ransomNote), m = len(magazine)

✅ Space Complexity: O(1)
👉 Since there are only 26 lowercase letters, the space used is constant.
"""

# Alternative Solution

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26  # Only lowercase letters

        for ch in magazine:
            freq[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            freq[idx] -= 1
            if freq[idx] < 0:
                return False

        return True



 
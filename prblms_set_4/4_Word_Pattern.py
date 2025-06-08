# 290. Word Pattern (Easy)
# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        charToWord, wordToChar = {}, {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True

"""
✅ Time Complexity: O(n)
👉 n = length of the pattern = number of words in s

✅ Space Complexity: O(k)
👉 Where k = number of unique characters/words (at most 26 and 1e4)
"""


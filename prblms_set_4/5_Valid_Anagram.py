# 242. Valid Anagram (Easy) - Done
# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        

"""
✅ Time: O(n)
✅ Space: O(1) → Because only 26 letters
"""

# Alternative Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0] * 26  # Only lowercase letters

        for ch_s, ch_t in zip(s, t):
            freq[ord(ch_s) - ord('a')] += 1
            freq[ord(ch_t) - ord('a')] -= 1

        return all(f == 0 for f in freq)

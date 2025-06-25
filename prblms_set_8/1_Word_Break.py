# 139. Word Break (Medium) - Done
# https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a DP array where dp[i] means: 
        # "Can we segment s[i:] using words from wordDict?"
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string is always "breakable"

        wordSet = set(wordDict)  # Set lookup is faster than list

        # Go from the end of the string to the beginning
        for i in range(len(s) - 1, -1, -1):
            for word in wordSet:
                # If the word fits in the remaining part of s
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    # If the rest of the string from here is breakable
                    if dp[i + len(word)]:
                        dp[i] = True
                        break  # No need to check further if already True

        return dp[0]


"""
Check from right to left:
i = 4: s[4:] = "code" ✅ in dict and dp[8] = True → dp[4] = True  
i = 0: s[0:4] = "leet" ✅ in dict and dp[4] = True → dp[0] = True  
"""


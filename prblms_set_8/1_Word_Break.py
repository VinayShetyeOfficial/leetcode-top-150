# 139. Word Break (Medium)
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

# Example
wordDict =
["leet","code"]

[False, False, False, False, False, False, False, False, True]
[False, False, False, False, False, False, False, False, True]
[False, False, False, False, False, False, False, False, True]
[False, False, False, False, True, False, False, False, True]
[False, False, False, False, True, False, False, False, True]
[False, False, False, False, True, False, False, False, True]
[False, False, False, False, True, False, False, False, True]

[True, False, False, False, True, False, False, False, True]

Stdout
   l     e      e     t      c      o      d      e   
[True, False, False, False, True, False, False, False, True]


"""
✅ Time Complexity:
O(n * m * k)

Where:
n = length of the string s
m = number of words in the dictionary (len(wordDict))
k = average length of the words in wordDict

Explanation:
The outer loop runs for each index i from len(s)-1 to 0 → O(n)
For each i, it iterates over all words in the wordSet → O(m)
For each word, the comparison s[i:i+len(word)] == word takes O(k) time in the worst case
So, total = O(n * m * k)

✅ Space Complexity:
O(n + m * k)

Explanation:
dp array takes O(n) space
wordSet stores all the words → O(m * k), assuming each word has average length k

✅ Final Answer:
Time Complexity: O(n * m * k)
Space Complexity: O(n + m * k)
"""









"""
# 49. Group Anagrams (Medium) - Done
# https://leetcode.com/problems/group-anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group anagrams: key = char count tuple, value = list of words
        anagrams = defaultdict(list)

        for word in strs:
            # Count the frequency of each letter in the word
            count = [0] * 26  # a to z
            for char in word:
                count[ord(char) - ord('a')] += 1

            # Use the tuple of counts as the key
            anagrams[tuple(count)].append(word)

        # Return the grouped anagrams
        return list(anagrams.values())


"""
✅ Time Complexity: O(n * k)
- n = number of words
- k = average length of each word
- We count letters (O(k)) instead of sorting (O(k log k))

✅ Space Complexity: O(n * k)
- To store all grouped anagrams
"""
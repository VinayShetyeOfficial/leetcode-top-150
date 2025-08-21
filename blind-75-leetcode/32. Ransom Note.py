# Link: https://leetcode.com/problems/ransom-note/description/

# ============================================
# Solution 1: Using count() with set
# ============================================
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True

"""
Time Complexity: O(n * m) in worst case
  - n = len(ransomNote), m = len(magazine)
  - For each unique character in ransomNote, count() scans the entire string
Space Complexity: O(k)
  - k = number of unique characters in ransomNote (for set)
"""

# ============================================
# Solution 2: Using Counter from collections
# ============================================
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for c in ransom_count:
            if ransom_count[c] > magazine_count.get(c, 0):
                return False
        return True

"""
Time Complexity: O(n + m)
  - n = len(ransomNote), m = len(magazine)
  - Counting both strings takes O(n + m)
  - Comparing counts takes O(k), k = unique characters
Space Complexity: O(n + m) 
  - Storing counts for both strings
"""

# ============================================
# Solution 3: Using array for lowercase letters
# ============================================
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26
        
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            index = ord(c) - ord('a')
            count[index] -= 1
            if count[index] < 0:
                return False
        
        return True

"""
Time Complexity: O(n + m)
  - n = len(ransomNote), m = len(magazine)
Space Complexity: O(1)
  - Fixed size array of length 26 for lowercase letters
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print("Can construct ransom note:", obj.canConstruct(ransomNote, magazine))

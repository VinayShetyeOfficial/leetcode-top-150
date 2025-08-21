# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/

# ============================================
# Solution 1: Using fixed-size frequency array
# ============================================
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26  # 26 lowercase letters

        # Step 1: Count frequency of each char
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # Step 2: Find first char with freq = 1
        for i in range(len(s)):
            if freq[ord(s[i]) - ord('a')] == 1:
                return i

        return -1

"""
Time Complexity: O(n) 
  - n = len(s), single pass for counting + single pass for finding first unique
Space Complexity: O(1) 
  - Fixed array of size 26 for lowercase letters
"""

# ============================================
# Solution 2: Using string.count (Brute-force)
# ============================================
class Solution2(object):
    def firstUniqChar(self, s):
        checked = set()
        for i, c in enumerate(s):
            if c not in checked and s.count(c) == 1:
                return i
            checked.add(c)
        return -1

"""
Time Complexity: O(n^2) 
  - s.count(c) is O(n) and we do it for each character
Space Complexity: O(n) for the checked set
"""

# ============================================
# Solution 3: Using dictionary (hashmap)
# ============================================
class Solution3(object):
    def firstUniqChar(self, s):
        char_count = {}
        
        # Step 1: Count frequency of each char
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
                
        # Step 2: Find first unique char
        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
                
        return -1

"""
Time Complexity: O(n) 
  - Counting + finding first unique pass
Space Complexity: O(k), k = number of distinct characters in s
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    s = "aabbc"
    
    obj1 = Solution()
    print("First unique char index (Solution 1):", obj1.firstUniqChar(s))
    
    obj2 = Solution2()
    print("First unique char index (Solution 2):", obj2.firstUniqChar(s))
    
    obj3 = Solution3()
    print("First unique char index (Solution 3):", obj3.firstUniqChar(s))

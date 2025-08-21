# Link: https://leetcode.com/problems/find-the-difference/description/

from collections import Counter

# ============================================
# Solution 1: Using Counter subtraction
# ============================================
class Solution1(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return (Counter(t) - Counter(s)).popitem()[0]

"""
Time Complexity: O(n + m) 
  - n = len(s), m = len(t), building counters
Space Complexity: O(k), k = number of distinct characters
"""

# ============================================
# Solution 2: Using brute-force count
# ============================================
class Solution2(object):
    def findTheDifference(self, s, t):
        for c in t:
            if t.count(c) > s.count(c):
                return c
        return ''

"""
Time Complexity: O(n*m) 
  - For each char in t, count in s and t (inefficient for long strings)
Space Complexity: O(1)
"""

# ============================================
# Solution 3: Using dictionary (hashmap)
# ============================================
class Solution3(object):
    def findTheDifference(self, s, t):
        char_count = {}
        
        # Count characters in t
        for c in t:
            char_count[c] = char_count.get(c, 0) + 1
        
        # Compare with counts in s
        for c in char_count:
            if char_count[c] > s.count(c):
                return c
        return ''

"""
Time Complexity: O(n + k*m) 
  - n = len(t), m = len(s), k = number of distinct characters
Space Complexity: O(k)
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    
    obj1 = Solution1()
    print("Difference char (Solution 1):", obj1.findTheDifference(s, t))
    
    obj2 = Solution2()
    print("Difference char (Solution 2):", obj2.findTheDifference(s, t))
    
    obj3 = Solution3()
    print("Difference char (Solution 3):", obj3.findTheDifference(s, t))

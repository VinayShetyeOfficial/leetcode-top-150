# Link: https://leetcode.com/problems/valid-anagram/description/

# ============================================
# Solution 1: Using count() with set
# ============================================

class Solution1(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
            
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True

"""
Time Complexity: O(n * m) 
    - n = length of s, m = unique characters in s (set(s)) 
    - s.count(char) and t.count(char) both take O(n)
Space Complexity: O(m)
    - For storing unique characters in set(s)
"""

# ============================================
# Solution 2: Sorting
# ============================================

class Solution2(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

"""
Time Complexity: O(n log n)
    - Sorting both strings takes O(n log n) time
Space Complexity: O(n)
    - For storing sorted lists of s and t
"""

# ============================================
# Solution 3: Using Counter / Hashmap
# ============================================

from collections import Counter

class Solution3(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

"""
Time Complexity: O(n)
    - Counting characters in both strings takes O(n)
Space Complexity: O(n)
    - For storing character counts in Counter dictionaries
"""

# ============================================
# Driver Code
# ============================================

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    obj1 = Solution1()
    obj2 = Solution2()
    obj3 = Solution3()

    print("Solution1:", obj1.isAnagram(s, t))
    print("Solution2:", obj2.isAnagram(s, t))
    print("Solution3:", obj3.isAnagram(s, t))

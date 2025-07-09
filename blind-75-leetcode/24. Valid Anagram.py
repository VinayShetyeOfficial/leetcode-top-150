# Link: https://leetcode.com/problems/valid-anagram/description/

# Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
            
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True

if __name__ == '__main__':
    obj = Solution()
    s = "anagram"
    t = "nagaram"
    print(obj.isAnagram(s, t))

# ----------------------

# Another Solution
class Solution(object):
    def isAnagram(self, s, t):
        t_sorted = sorted(t)   # ['a', 'a', 'a', 'g', 'm', 'n', 'r'] 
        s_sorted = sorted(s)   # ['a', 'a', 'a', 'g', 'm', 'n', 'r'] 
        
        return t_sorted == s_sorted
        # return ''.join(sorted(s)) == ''.join(sorted(t))

        
if __name__ == '__main__':
    obj = Solution()
    s = "anagram"
    t = "nagaram"
    print(obj.isAnagram(s, t))

# ----------------------

# Another Solution
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        s = dict(Counter(s))   # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        t = dict(Counter(t))   # {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

        return s == t          # True
        
if __name__ == '__main__':
    obj = Solution()
    s = "anagram"
    t = "nagaram"
    print(obj.isAnagram(s, t))
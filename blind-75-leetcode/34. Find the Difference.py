# Link: https://leetcode.com/problems/find-the-difference/description/

# Find the Difference
from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        return (Counter(t) - Counter(s)).popitem()[0]
                
# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "a"
    t = "aa"
    print(obj.findTheDifference(s, t))

# ----------------------

# Another Solution
class Solution(object):
    def findTheDifference(self, s, t):
        for c in t:
            if t.count(c) > s.count(c):
                return c
            
# ----------------------

# Another Solution
class Solution(object):
    def findTheDifference(self, s, t):
        char_count = {}
        
        for c in t:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        for c in char_count:
            if char_count[c] > s.count(c):
                return c
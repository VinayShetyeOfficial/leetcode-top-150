# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/

# First Unique Character in a String
class Solution(object):
    def firstUniqChar(self, s):
        checked = set()
        for i, c in enumerate(s):
            if c not in checked and s.count(c) == 1:
                    return i
            checked.update({c})
                
        return  -1         
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    s = "aabb"
    print(obj.firstUniqChar(s))

# ----------------------

# Another Solution
class Solution(object):
    def firstUniqChar(self, s):
        char_count = {}
        
        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
                
        for i, c in enumerate(s):
            if char_count[c] == 1:
                return i
                
        return -1

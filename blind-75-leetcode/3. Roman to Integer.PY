# Link: https://leetcode.com/problems/roman-to-integer/description/

# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }
        
        total = 0
        prevVal = 0
        
        for char in reversed(s):
            curVal = roman_map[char]
            
            if curVal < prevVal:
                total -= curVal
            else:
                total += curVal
                
            prevVal = curVal
                
        return total 
               
if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("XIV"))

"""
Time Complexity (TC): O(n)
- We traverse the string once (n = length of s).
- Dictionary lookups are O(1).

Space Complexity (SC): O(1)
- Only fixed-size dictionary and a few variables are used.
"""


# ========================================
# Alternate Implementation
class Solution(object):
    def romanToInt(self, s):
        rom_num = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }
        
        s = s.upper()
        res = rom_num[s[0]]
        
        for i in range(1, len(s)):
            if rom_num[s[i-1]] < rom_num[s[i]]:
                res -= 2 * rom_num[s[i-1]]
            res += rom_num[s[i]]
        
        return res 
               
if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("XIV"))

"""
Time Complexity (TC): O(n)
- We go through the string once (n = length of s).
- Dictionary access is O(1).

Space Complexity (SC): O(1)
- Uses constant extra variables + fixed dictionary.
"""

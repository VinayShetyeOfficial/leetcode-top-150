# Link: https://leetcode.com/problems/roman-to-integer/description/

# Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        rom_num = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L': 50, 
            'C': 100, 
            'D':500, 
            'M': 1000
            }
        
        s = s.upper()
        res = rom_num[s[0]]
        
        for i in range(1, len(s)):
            if(rom_num[s[i-1]] < rom_num[s[i]]):
                res -= 2*rom_num[s[i-1]]
            res += rom_num[s[i]]
        
        return res 
               
if __name__ == "__main__":
    obj = Solution()
    print(obj.romanToInt("XIV"))
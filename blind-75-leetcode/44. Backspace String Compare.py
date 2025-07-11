# Link: https://leetcode.com/problems/backspace-string-compare/description/

# Backspace String Compare
class Solution(object):
    def backspaceCompare(self, s, t):
        def remove(s):
            stk = []
            
            for ch in s:
                if ch == "#":
                    if stk: stk.pop()
                else:
                    stk.append(ch)
            return stk
        return remove(s) == remove(t)
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    
    s = "b"
    t = "a#c"
    print(obj.backspaceCompare(s, t))
    
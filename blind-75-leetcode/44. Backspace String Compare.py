# ============================================
# Backspace String Compare - LeetCode
# ============================================

# ---------------------------
# Solution: Using stack
# ---------------------------
class Solution(object):
    def backspaceCompare(self, s, t):
        def remove(string):
            stk = []
            for ch in string:
                if ch == "#":
                    if stk:
                        stk.pop()
                else:
                    stk.append(ch)
            return stk
        
        return remove(s) == remove(t)

"""
Time Complexity (TC): O(n + m)
   - n = len(s), m = len(t)
   - Each character is processed once
Space Complexity (SC): O(n + m)
   - Stack for s and t may store all characters in worst case
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    
    s = "b"
    t = "a#c"
    print("Result:", obj.backspaceCompare(s, t))  # Output: False

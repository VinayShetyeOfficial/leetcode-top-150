# Link: https://leetcode.com/problems/reverse-string/description/

# ============================================
# Solution: Two-pointer approach (In-place)
# ============================================
class Solution:
    def reverseString(self, s):
        """
        Reverses the list of characters in-place.
        :type s: List[str]
        :rtype: List[str]
        """
        low = 0
        high = len(s) - 1
        
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        
        return s

        # Alternate approaches (all in-place):
        # 1. s[:] = s[::-1]; return s
        # 2. s.reverse(); return s

"""
Time Complexity: O(n) for traversing half of the list
Space Complexity: O(1) extra space
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    s = ["h","e","l","l","o"]
    print("Reversed String:", obj.reverseString(s))

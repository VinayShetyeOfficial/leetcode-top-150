# Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

# ============================================
# Solution: Binary Search
# ============================================

# Mock guess API (for local testing only)
def guess(num):
    picked = 12   # Example: the hidden picked number
    if num < picked:
        return 1
    elif num > picked:
        return -1
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            res = guess(mid)
            
            if res == 0:         # Found the picked number
                return mid
            elif res < 0:        # mid > picked
                high = mid - 1
            else:                # mid < picked
                low = mid + 1
        
        return -1  # Just a fallback (shouldn't happen on LeetCode)

"""
Time Complexity: O(log n) 
  - Binary search halves the search space each step
Space Complexity: O(1) 
  - Only a few variables used, no extra data structures
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    n = 30
    print("Picked number is:", obj.guessNumber(n))

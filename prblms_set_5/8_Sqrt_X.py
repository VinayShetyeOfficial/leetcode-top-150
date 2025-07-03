# 69. Sqrt(x) (Easy) - Done
# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # right is the floor of sqrt(x)

"""
✅ Time Complexity: O(log x)
👉 Converges fast, logarithmic iterations

✅ Space Complexity: O(1)
👉 Constant space
"""

# Alternate
class Solution:
    def mySqrt(self, x: int) -> int:
        res = x

        if x == 0:
            return 0

        while True:
            res = (res + x / res) / 2

            if round(res*res) == x:
                break 
                
        return int(res)
    
    
"""
✅ Time Complexity: O(log x)
👉 Newton's Method converges very fast — roughly in log x iterations.

✅ Space Complexity: O(1)
👉 Uses constant extra space (only a few variables).
"""

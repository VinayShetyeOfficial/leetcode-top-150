# Link: https://leetcode.com/problems/sqrtx/

# ============================================
# Solution 1: Binary Search
# ============================================

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            sqProd = mid * mid

            if sqProd == x:
                return mid
            elif sqProd < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

"""
Time Complexity (TC): O(log n) 
- Each iteration halves the search space.

Space Complexity (SC): O(1) 
- Only constant variables are used.
"""

# ============================================
# Solution 2: Newton's Method (Babylonian)
# ============================================

class AltSolution:
    def sqrt_of_num(self, num: int) -> int:
        res = num  # Initial guess
        
        while True:
            res = (res + num / res) / 2  # Update guess
            
            # Break when res stabilizes (close enough to true sqrt)
            if round(res * res) == num:
                break
        
        return int(res)
        # return int(num**0.5)   # ⭐ Optional shortcut

"""
Time Complexity (TC): O(log n) 
- Converges very fast (logarithmic number of iterations).

Space Complexity (SC): O(1) 
- Uses constant extra space.
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    # Binary Search Solution
    obj1 = Solution()
    print("Binary Search Method:")
    print("Sqrt(4) =", obj1.mySqrt(4))      # Output: 2
    print("Sqrt(8) =", obj1.mySqrt(8))      # Output: 2
    print("Sqrt(36) =", obj1.mySqrt(36))    # Output: 6

    # Newton's Method Solution
    obj2 = AltSolution()
    print("\nNewton's Method:")
    print("Sqrt(4) =", obj2.sqrt_of_num(4))   # Output: 2
    print("Sqrt(8) =", obj2.sqrt_of_num(8))   # Output: 2
    print("Sqrt(36) =", obj2.sqrt_of_num(36)) # Output: 6

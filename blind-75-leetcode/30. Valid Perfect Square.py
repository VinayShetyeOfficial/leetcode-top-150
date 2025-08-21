# Link: https://leetcode.com/problems/valid-perfect-square/description/

# ============================================
# Valid Perfect Square
# ============================================
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True  # 0 and 1 are perfect squares

        left, right = 2, num // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False

        # Optional one-liner
        # return math.floor(num**0.5)**2 == num

"""
Time Complexity: O(log(num)) 
  - Binary search from 2 to num//2
Space Complexity: O(1)
"""

# ============================================
# Driver code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    num = 14
    print(obj.isPerfectSquare(num))  # ✅ fixed typo from sPerfectSquare to isPerfectSquare

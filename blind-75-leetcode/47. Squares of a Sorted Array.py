# ============================================
# Squares of a Sorted Array - LeetCode
# ============================================

from typing import List

# ---------------------------
# Solution 1: Two Pointers (O(n))
# ---------------------------
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Final sorted squares
        left, right = 0, n - 1
        pos = n - 1  # Position to insert next largest square

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result

"""
Time Complexity (TC): O(n)
   - Single pass through the array
Space Complexity (SC): O(n)
   - Result array of size n
"""

# ---------------------------
# Solution 2: Square + Sort (O(n log n))
# ---------------------------
class Solution2(object):
    def sortedSquares(self, nums):
        nums = [x**2 for x in nums]  # Square all elements
        nums.sort()                   # Sort the squares
        return nums

"""
Time Complexity (TC): O(n log n)
   - Sorting dominates
Space Complexity (SC): O(n)
   - List of squared elements
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    
    # Test Solution1
    obj1 = Solution1()
    print("Solution1:", obj1.sortedSquares(nums.copy()))
    
    # Test Solution2
    obj2 = Solution2()
    print("Solution2:", obj2.sortedSquares(nums.copy()))

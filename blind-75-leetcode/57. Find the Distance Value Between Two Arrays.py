# ============================================
# Find the Distance Value Between Two Arrays - LeetCode
# ============================================

from typing import List

# Approach 1: Nested Loops
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num1 in arr1:
            is_valid = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_valid = False
                    break
            if is_valid:
                count += 1
        return count

# Approach 2: Using all() for readability
class SolutionAlt:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num1 in arr1:
            if all(abs(num1 - num2) > d for num2 in arr2):
                count += 1
        return count

# Optimized Approach: Binary Search after sorting arr2
import bisect
class SolutionOptimized:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for num in arr1:
            # find insertion position
            idx = bisect.bisect_left(arr2, num)
            left_safe = idx == 0 or abs(num - arr2[idx-1]) > d
            right_safe = idx == len(arr2) or abs(num - arr2[idx]) > d
            if left_safe and right_safe:
                count += 1
        return count

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    arr1 = [1,4,2,3]
    arr2 = [-4,-3,6,10,20,30]
    d = 3
    
    obj = Solution()
    print(obj.findTheDistanceValue(arr1, arr2, d))  # Nested Loops
    
    obj_alt = SolutionAlt()
    print(obj_alt.findTheDistanceValue(arr1, arr2, d))  # Using all()
    
    obj_opt = SolutionOptimized()
    print(obj_opt.findTheDistanceValue(arr1, arr2, d))  # Optimized Binary Search

"""
Time Complexity (TC):
- Nested Loops / all(): O(n * m), n = len(arr1), m = len(arr2)
- Optimized Binary Search: O(n log m) for sorting + O(n log m) for binary search => O(n log m)

Space Complexity (SC):
- Nested Loops / all(): O(1)
- Optimized: O(1) extra space (sorting done in-place)
"""

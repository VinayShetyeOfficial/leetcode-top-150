# Link: https://leetcode.com/problems/move-zeroes/

from typing import List

# ============================================
# Solution 1: Two-pointer swap
# ============================================
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# ============================================
# Solution 2: Move non-zero elements first, then fill zeros
# ============================================
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1
                
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
        return nums

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# ============================================
# Solution 3: Using list comprehension
# ============================================
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:] = [val for val in nums if val != 0] + [0] * nums.count(0)
        return nums

"""
Time Complexity: O(n)
Space Complexity: O(n) due to creating a new list
"""

# ============================================
# Solution 4: Pop and insert (Not efficient)
# ============================================
class Solution4:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(n-1, 0)
        return nums

"""
Time Complexity: O(n^2) — inefficient for large lists
Space Complexity: O(1)
"""

# ============================================
# Driver code
# ============================================

if __name__ == '__main__':
    nums_list = [0,1,0,3,12]

    print("Solution 1:", Solution1().moveZeroes(nums_list[:]))
    print("Solution 2:", Solution2().moveZeroes(nums_list[:]))
    print("Solution 3:", Solution3().moveZeroes(nums_list[:]))
    print("Solution 4:", Solution4().moveZeroes(nums_list[:]))

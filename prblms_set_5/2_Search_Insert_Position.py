# 35. Search Insert Position (Easy) - Done
# https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Uses binary search to find the index of target in nums.
        If not found, returns the index where it should be inserted.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Target not found, return insert position
        return left


"""
✅ Time Complexity: O(log n)
👉 Binary search halves the range each time

✅ Space Complexity: O(1)
👉 Constant space
"""


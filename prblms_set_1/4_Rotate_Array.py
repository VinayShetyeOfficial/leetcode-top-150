# 189. Rotate Array (Medium) - Done
# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """

        n = len(nums)
        k = k % n  # Handle cases where k >= n

        # Step 1: Reverse the entire array
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: Reverse the first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: Reverse the remaining n - k elements
        l, r = k, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

"""
✅ Time Complexity: O(n)
👉 Each reversal is O(n), and we perform it 3 times.

✅ Space Complexity: O(1)
👉 In-place rotation with no additional space used.
"""

# ===========================================
# Other Direct Solution
class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 2 and k%2 == 1: 
            nums[:] = nums[::-1]
        else:
            nums[:] = nums[len(nums)-k:] + nums[0:len(nums)-k]
            
        return nums

"""
✅ Time Complexity: O(n)
👉 Slice and concatenation each take O(n), where n = len(nums)

✅ Space Complexity: O(n)
👉 nums[len(nums)-k:] + nums[0:len(nums)-k] creates a temporary copy of the list
"""
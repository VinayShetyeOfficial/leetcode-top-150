# 189. Rotate Array (Medium) - Done
# https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """

        n = len(nums)
        k = k % n  # Handle cases where k >= n
          
        """
        ✅ Explanation of the k == 0 check:
        - If k == 0, you're rotating by 0 steps → no change needed.        
        - If k % n == 0, then you're rotating by a multiple of the array length → it comes back to the original array.
        """
        if k == 0:
            return  # No rotation needed

        # Step 1: Reverse the entire array
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: Reverse the first k elements
        l, r = 0, k - 1     # l, r = 0, k           --> for right to left rotation
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: Reverse the remaining n - k elements
        l, r = k, n - 1     # l, r = k + 1, n - 1  --> for right to left rotation
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
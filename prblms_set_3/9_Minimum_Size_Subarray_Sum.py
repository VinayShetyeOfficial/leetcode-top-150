# 209. Minimum Size Subarray Sum (Medium) - Done
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a contiguous subarray
        of which the sum is at least target. Returns 0 if none exists.
        """

        min_length = float('inf')  # Initialize with infinity
        window_sum = 0
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            # Shrink window as long as the current sum ≥ target
            while window_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)
                window_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length

"""
✅ Time Complexity: O(n)
👉 Each element is visited at most twice (once by `right`, once by `left`)

✅ Space Complexity: O(1)
👉 No additional space used (other than variables)
"""
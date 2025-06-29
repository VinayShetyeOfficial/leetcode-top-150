# 16. 3Sum Closest (Medium) - Done
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Returns the sum of three integers in nums that is closest to the target.
        """

        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest_sum if this is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match
                    return current_sum

        return closest_sum


"""
✅ Time Complexity: O(n^2)
👉 Outer loop O(n), inner loop (two-pointer) O(n) = O(n^2) total

✅ Space Complexity: O(1) (ignoring the output)
👉 No extra space used for computation
"""

'''
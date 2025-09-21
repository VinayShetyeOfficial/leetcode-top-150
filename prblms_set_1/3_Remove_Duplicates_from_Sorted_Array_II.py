# 80. Remove Duplicates from Sorted Array II (Medium) - Done
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Removes duplicates from sorted array so that each element appears at most twice.
        Returns the new length of the modified array.
        """

        l, r = 0, 0  # l is the write pointer, r is the read pointer

        while r < len(nums):
            count = 1

            # Count how many times the current number repeats
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            # Write the number at most twice
            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            # Move to the next number
            r += 1

        return l

"""
✅ Time Complexity: O(n)
👉 We traverse the array once with two pointers.

✅ Space Complexity: O(1)
👉 The solution is done in-place using only variables for counting and tracking pointers.
"""
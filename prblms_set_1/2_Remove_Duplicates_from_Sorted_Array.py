# 26. Remove Duplicates from Sorted Array (Easy) - Done
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Removes duplicates from sorted array in-place.
        Returns the number of unique elements (k),
        and modifies nums such that the first k elements are the unique values.
        """

        # Edge case: empty array
        if not nums:
            return 0

        # Initialize write pointer at index 1 (first element is always unique)
        write_ptr = 1

        # Start from the second element and compare with previous
        for read_ptr in range(1, len(nums)):
            if nums[read_ptr] != nums[read_ptr - 1]:
                # Found a new unique element
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1  # Move write_ptr to next slot

        # After loop, write_ptr is the count of unique elements
        return write_ptr


"""
✅ Time Complexity: O(n)
👉 We traverse the array once, doing constant-time work per element.

✅ Space Complexity: O(1)
👉 All operations are done in-place. Only a couple of pointers are used.
"""
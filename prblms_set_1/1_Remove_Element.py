# 27. Remove Element (Easy) - Done
# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Removes all instances of val from nums in-place.
        Returns the number of elements that are not equal to val.
        """

        # Pointer to keep track of where to write the next valid element
        write_ptr = 0

        # Iterate over the array using read_ptr
        for read_ptr in range(len(nums)):
            if nums[read_ptr] != val:
                # Copy valid element to the front (write_ptr position)
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1  # Move write_ptr to next position

        # At this point, first 'write_ptr' elements are valid
        return write_ptr

"""
⏱️ Time & Space Complexity:
---------------------------
✅ Time Complexity: O(n)
👉 We iterate through the array once (single pass).
    - Each element is checked exactly once.

✅ Space Complexity: O(1)
👉 No extra space is used — done entirely in-place.
    - Only a couple of integer variables are used (pointers).
"""
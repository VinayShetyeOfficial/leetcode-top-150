# 66. Plus One (Easy)
# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Adds one to the number represented by the digit array.
        Handles carry by setting 9 to 0 and inserting 1 at the front if needed.
        """

        # Traverse digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, return early
            digits[i] = 0  # Set current to 0 and carry over to next digit

        # All digits were 9 (e.g. [9, 9, 9]), we need to insert 1 at the beginning
        return [1] + digits


"""
✅ Time Complexity: O(n)
👉 In the worst case, we visit all digits

✅ Space Complexity: O(1)
👉 In-place update (excluding output array)
"""
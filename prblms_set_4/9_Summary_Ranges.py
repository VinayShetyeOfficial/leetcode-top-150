# 228. Summary Ranges (Easy)
# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Returns the smallest sorted list of ranges that cover all numbers in nums.
        Each range is represented as "a->b" or "a" if it’s a single element.
        """

        if not nums:
            return []

        result = []
        start = 0  # Start index of current range

        for i in range(1, len(nums) + 1):
            # End of range detected (or end of list)
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))  # Single element
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")  # Range
                start = i  # Update start for next range

        return result

"""
✅ Time Complexity: O(n)
👉 One pass through the list

✅ Space Complexity: O(1) (excluding output list)
👉 Only a few variables are used
"""
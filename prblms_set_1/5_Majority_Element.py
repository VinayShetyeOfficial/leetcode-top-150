# 169. Majority Element (Easy) - Done
# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Returns the element that appears more than ⌊n / 2⌋ times.
        Uses Boyer-Moore Voting Algorithm for O(n) time and O(1) space.
        """

        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n  # Choose new candidate
                
            # Update count based on current value
            count += 1 if n == res else -1

        return res

"""
✅ Time Complexity: O(n)
👉 Single pass through the array.

✅ Space Complexity: O(1)
👉 No extra space used; only two variables (res, count).
"""


# ===========================================
# Base Solution (Not Fast)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res

"""
✅ Time Complexity: O(n)
👉 Each number in the array is visited once

✅ Space Complexity: O(n)
👉 Hash map stores up to n unique elements in the worst case (all numbers different)
"""
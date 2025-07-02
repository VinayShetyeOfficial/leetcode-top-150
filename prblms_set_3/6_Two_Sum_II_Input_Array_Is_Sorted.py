# 167. Two Sum II - Input Array Is Sorted - Done
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Works for both Problems `Two Sum I & II` 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, idx + 1]
            seen[num] = idx


# Alternate Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers that add up to target in a sorted array.
        Returns 1-indexed positions using two-pointer approach.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # Problem guarantees there is one solution, so no need for return -1 case
        
"""
✅ Time Complexity: O(n)
👉 One pass through the list

✅ Space Complexity: O(1)
👉 Only two pointers used
"""
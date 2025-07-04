# 15. 3Sum (Medium) - Done
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Returns all unique triplets [a, b, c] such that a + b + c = 0.
        Uses sorting and two-pointer technique to avoid duplicates.
        """

        result = []
        nums.sort()  # Sort first for two-pointer logic and duplicate handling

        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move left pointer and skip duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result


"""
✅ Time Complexity: O(n^2)
👉 Outer loop O(n), inner loop (two-pointer) O(n) = O(n^2) total

✅ Space Complexity: O(1) (ignoring the output)
👉 No extra space used for computation
"""
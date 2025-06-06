# 238. Product of Array Except Self (Medium) - Done
# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all elements
        in nums except nums[i], computed in O(n) time and without division.
        """

        n = len(nums)
        result = [1] * n  # Output array to store final results

        # Step 1: Compute prefix product for each index
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        # Step 2: Compute postfix product and multiply with prefix
        postfix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result

"""
✅ Time Complexity: O(n)
👉 Two linear passes through the array.

✅ Space Complexity: O(1) extra space (excluding result)
👉 Uses only prefix and postfix variables. The result array is not counted against space as per problem constraints.
"""
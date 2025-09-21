# 55. Jump Game (Medium) - Done
# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: ist[int]) -> bool:
        """
        Returns True if you can reach the last index starting from the first.
        Uses greedy backward approach.
        """

        goal = len(nums) - 1  # Start from the last index

        # Traverse from the end to the beginning
        for i in range(len(nums) - 1, -1, -1):
            # If current index can jump to or beyond the goal
            if i + nums[i] >= goal:
                goal = i  # Move goal to the current index

        # If goal has moved to the start, we can reach the end
        return goal == 0

"""
✅ Time Complexity: O(n)
👉 Single pass through the array from right to left.

✅ Space Complexity: O(1)
👉 Only a single variable (goal) is used.
"""
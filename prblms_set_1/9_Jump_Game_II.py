# 55. Jump Game II (Medium) - Done
# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: list[int]) -> int:
        """
        Returns the minimum number of jumps to reach the last index.
        Uses a greedy, level-based approach similar to BFS.
        """

        res = 0         # Number of jumps
        l, r = 0, 0     # Window of indices reachable in current jump

        while r < len(nums) - 1:
            farthest = 0

            # Check the furthest we can jump in the current range
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # Move the window to the next range
            l = r + 1
            r = farthest
            res += 1

        return res

"""
✅ Time Complexity: O(n)
👉 Each element is visited at most once within the current window.

✅ Space Complexity: O(1)
👉 Only a few integer variables are used.
"""

# Alternative Solution 
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach
        the last index from the first index of the array.
        """

        jumps = 0  # Total number of jumps made
        current_jump_end = 0  # The farthest point reachable in the current jump
        farthest_reach = 0  # The farthest point reachable from current window

        # We don't need to jump from the last index
        for i in range(len(nums) - 1):
            # Update the farthest reach from current position
            farthest_reach = max(farthest_reach, i + nums[i])

            # If we've reached the end of the current jump,
            # it's time to make another jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest_reach

        return jumps

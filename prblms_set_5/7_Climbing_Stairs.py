# 70. Climbing Stairs (Easy) - Done
# https://leetcode.com/problems/climbing-stairs

# Best Video: https://www.youtube.com/shorts/UY6d4cv-0RI
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i - 2] + steps[i - 1])
        return steps[-1]
    
    
# Alternate Solution
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Returns the number of distinct ways to climb to the top.
        Uses bottom-up DP with O(1) space.
        """
        if n == 1:
            return 1

        prev = 1  # ways to reach step 0
        curr = 1  # ways to reach step 1

        for _ in range(2, n + 1):
            next_step = prev + curr
            prev = curr
            curr = next_step

        return curr

"""
✅ Time Complexity: O(n)
👉 Single pass from 2 to n

✅ Space Complexity: O(1)
👉 Only two variables used
"""
# Link: https://leetcode.com/problems/climbing-stairs/

# ============================================
# Solution: Fibonacci Iterative Approach
# ============================================

class Solution(object):
    def climbStairs(self, n):
        prev_step = 0   # Represents dp[i-2]
        curr_step = 1   # Represents dp[i-1]
        
        for i in range(n):
            next_step = prev_step + curr_step
            prev_step = curr_step
            curr_step = next_step
            
        return curr_step

"""
Time Complexity (TC): O(n)
- We iterate from 1 to n once.

Space Complexity (SC): O(1)
- Only constant variables (prev_step, curr_step, next_step).
"""

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    print("Climb 2 steps:", obj.climbStairs(2))   # Output: 2
    print("Climb 3 steps:", obj.climbStairs(3))   # Output: 3
    print("Climb 4 steps:", obj.climbStairs(4))   # Output: 5
    print("Climb 5 steps:", obj.climbStairs(5))   # Output: 8

# 172. Factorial Trailing Zeroes (Medium) - Done
# https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


"""
✅ Time Complexity: O(log₅ n)
✅ Space Complexity: O(1)
"""
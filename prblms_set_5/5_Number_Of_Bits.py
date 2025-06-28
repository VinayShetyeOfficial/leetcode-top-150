# 191. Number of 1 Bits (Easy) - Done
# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Returns the number of '1' bits (set bits) in the binary representation of n.
        Uses Brian Kernighan's algorithm for efficient bit counting.
        """
        count = 0
        while n:
            n &= (n - 1)  # Clear the least significant set bit
            count += 1
        return count

"""
✅ Time Complexity: O(k)
👉 k = number of set bits (more efficient than O(32) if few 1s)

✅ Space Complexity: O(1)
👉 Constant space
"""
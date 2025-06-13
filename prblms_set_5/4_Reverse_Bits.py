# 190. Reverse Bits (Easy) - Done
# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverses the bits of a 32-bit unsigned integer.
        Uses bitwise shifting and masking for efficiency.
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # Add the last bit of n to result
            n >>= 1  # Shift n to the right by 1 to process the next bit
        return result


"""
✅ Time: O(1)
👉 Fixed 32 iterations regardless of input

✅ Space: O(1)
👉 Constant space usage
"""
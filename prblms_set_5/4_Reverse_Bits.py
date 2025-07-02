# 190. Reverse Bits (Easy) - Done
# https://leetcode.com/problems/reverse-bits

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        num = bin(n)[2:]
        num32bit = '0' * (32 - len(num)) + num

        for i in range(len(num32bit)):
            res += 2 ** i if num32bit[i] == '1' else 0

        return res
    

# Alternative Solution
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
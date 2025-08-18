# Link: https://leetcode.com/problems/reverse-bits/

# ============================================
# Reverse Bits
# ============================================

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Convert integer to 32-bit binary string
        k = format(n, '032b')
        # Reverse the binary string
        rev = k[::-1]
        # Convert back to integer
        return int(rev, 2)
        # Optional one-liner: return int(str('{0:032b}'.format(n))[::-1], 2)

"""
Time Complexity (TC): O(1)
- We always process 32 bits, independent of input value.

Space Complexity (SC): O(1)
- We store a fixed-length 32-bit string.
"""

# ============================================
# Driver Code
# ============================================

if __name__ == '__main__':
    obj = Solution()
    # Input can be provided as integer (decimal)
    n = 43261596  # Equivalent to binary 00000010100101000001111010011100
    print("Reversed Bits:", obj.reverseBits(n))  # Output: 964176192

# Link: https://leetcode.com/problems/power-of-two/description/

# ============================================
# Power of Two
# ============================================

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Check if a number is a power of two using bit manipulation.
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0

"""
How it works:
-------------
- A number n that is a power of two has exactly one '1' in its binary representation.
- Subtracting 1 flips all bits after that '1'.
- So doing n & (n - 1) will always give 0 for powers of two.

Example:
--------
1) n = 8 → 1000
   n-1 = 7 → 0111
   1000 & 0111 = 0000 ✅ Power of two

2) n = 10 → 1010
   n-1 = 9 → 1001
   1010 & 1001 = 1000 ❌ Not a power of two
"""

# ============================================
# Driver Code
# ============================================

if __name__ == '__main__':
    obj = Solution()
    num = 16
    print(f"Is {num} a power of two? {obj.isPowerOfTwo(num)}")  # Output: True

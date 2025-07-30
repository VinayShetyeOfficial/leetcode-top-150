# Link: https://leetcode.com/problems/power-of-two/description/

# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

    
if __name__ == '__main__':
    obj = Solution()
    num = 16
    print(obj.isPowerOfTwo(num))


'''
Example:
--------
Take n = 8 → 1000
Then n - 1 = 7 → 0111
Now do:
  1000   (8)
& 0111   (7)
= 0000
✅ So result is 0 → which means n is a power of 2

Example:
--------
❌ Now take n = 10 → 1010
Then n - 1 = 9 → 1001
Now:
  1010
& 1001
= 1000   → Not 0 → So not a power of 2
'''
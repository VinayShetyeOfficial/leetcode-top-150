# Link: https://leetcode.com/problems/power-of-two/description/

# Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

    
if __name__ == '__main__':
    obj = Solution()
    num = 16
    print(obj.isPowerOfTwo(num))
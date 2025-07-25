# Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/

# Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num):
    picked = 12
    
    if num < picked:
        return 1
    elif num > picked:
        return -1
    
    return 0
    
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = (low + high)//2

            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1
        
        return low
        
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    num = 30
    print(obj.guessNumber(num))

        
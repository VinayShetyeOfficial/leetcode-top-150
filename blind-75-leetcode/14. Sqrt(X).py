# Link: https://leetcode.com/problems/sqrtx/

# Square Root Of Number
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            sqProd = mid * mid
            if sqProd == x:
                return mid
            elif sqProd < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
    
# ============================================

# Alternate Solution

class Solution(object):
    def sqrt_of_num(self, num):
        
        res = num
        
        while True:
            res = ( res + num / res ) / 2
            
            if round(res*res) == num:
                break
        
        return int(res)
        # return int(x**0.5)          # ⭐ Optional 
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    print(obj.sqrt_of_num(36))

# Link: https://leetcode.com/problems/sqrtx/

# Square Root Of Number
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

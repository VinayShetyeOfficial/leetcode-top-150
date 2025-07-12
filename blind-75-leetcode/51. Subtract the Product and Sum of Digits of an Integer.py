# Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

# Subtract the Product and Sum of Digits of an Integer
class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sum = 0
        while n > 0:
            r = n % 10
            prod *= r
            sum += r
            n = n//10

        return prod - sum

        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 234
    print(obj.subtractProductAndSum(n))
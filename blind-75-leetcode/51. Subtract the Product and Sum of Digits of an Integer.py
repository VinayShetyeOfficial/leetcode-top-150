# ============================================
# Subtract the Product and Sum of Digits of an Integer - LeetCode
# ============================================

class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1
        sum_ = 0  # Avoid using Python built-in 'sum'
        
        while n > 0:
            r = n % 10
            prod *= r
            sum_ += r
            n = n // 10

        return prod - sum_

# ============================================
# Driver Code
# ============================================
if __name__ == '__main__':
    obj = Solution()
    n = 234
    print(obj.subtractProductAndSum(n))  # Output: 15

"""
Time Complexity (TC): O(d)
- Where d is the number of digits in n. Each digit is processed once.

Space Complexity (SC): O(1)
- Only two variables are used for product and sum, no extra space required.
"""

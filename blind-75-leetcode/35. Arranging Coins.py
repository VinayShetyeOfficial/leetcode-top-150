# Link: https://leetcode.com/problems/arranging-coins/description/

# Arranging Coins
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins_used = (mid * (mid + 1)) // 2  # Sum of first 'mid' natural numbers
            
            if coins_used == n:  # Perfect staircase
                return mid
            elif coins_used < n:  # Can still build more rows
                left = mid + 1
            else:  # Too many coins used, reduce search range
                right = mid - 1
                
        return right  # 'right' will be at the last valid row count

# ============================================

# Alternate Solution

class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        while n >=0:
            n -= i
            i += 1
        return i - 1
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.arrangeCoins(n))

# ============================================

# Another Solution
class Solution(object):
    def arrangeCoins(self, n):
        if n == 1:
            return n
        
        step = 0
        coins = 1
        
        while n > 0:
            n = n - coins
            coins += 1
            
            if n >= 0:
                step += 1
            else:
                break
            
        return step
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.arrangeCoins(n))



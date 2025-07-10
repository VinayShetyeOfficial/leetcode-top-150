# Link: https://leetcode.com/problems/arranging-coins/description/

# Arranging Coins
class Solution(object):
    def arrangeCoins(self, n):
        i = 1
        while n >=0 i:
            n -= i
            i += 1
        return i - 1
    
# Driver code
if __name__ == '__main__':
    obj = Solution()
    n = 10
    print(obj.arrangeCoins(n))

# ----------------------

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



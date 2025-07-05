# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        min_so_far = prices[0]
        max_profit = 0
        
        for current_price in prices:
            max_profit = max(max_profit, current_price - min_so_far)
            min_so_far = min(min_so_far, current_price)
            
        return max_profit
        
# Driver code
if __name__ == '__main__':
    obj = Solution()
    prices = [7,1,5,3,6,4]
    
    print(obj.maxProfit(prices))
    
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# ============================================
# Best Time to Buy and Sell Stock I
# Single transaction
# ============================================

class BestTimeBuySellI(object):
    def maxProfit(self, prices):
        min_so_far = prices[0]
        max_profit = 0
        
        for current_price in prices:
            max_profit = max(max_profit, current_price - min_so_far)
            min_so_far = min(min_so_far, current_price)
            
        return max_profit

"""
Time Complexity (TC): O(n)
- Single pass through the prices list.

Space Complexity (SC): O(1)
- Only two variables used.
"""

# ============================================
# Best Time to Buy and Sell Stock II
# Multiple transactions
# ============================================

class BestTimeBuySellII(object):
    def maxProfit(self, prices):
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit

"""
Time Complexity (TC): O(n)
- Single pass through the prices list.

Space Complexity (SC): O(1)
- Only one variable used for accumulation.
"""

# ============================================
# Driver Code
# ============================================

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]

    # Stock I
    obj1 = BestTimeBuySellI()
    print("Max Profit (Single Transaction):", obj1.maxProfit(prices))  # Output: 5

    # Stock II
    obj2 = BestTimeBuySellII()
    print("Max Profit (Multiple Transactions):", obj2.maxProfit(prices))  # Output: 7

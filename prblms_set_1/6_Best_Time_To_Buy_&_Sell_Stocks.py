# 121. Best Time to Buy and Sell Stock (Easy) - Done
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Returns the maximum profit from buying and selling one stock.
        You must buy before you sell.
        """

        stock_price = prices[0]  # Track minimum price so far
        max_profit = 0  # Track max profit seen so far

        for price in prices:
            # Update stock_price if a lower price is found
            if price < stock_price:
                stock_price = price

            # Calculate potential profit if sold today
            max_profit = max(max_profit, price - stock_price)

        return max_profit

"""
✅ Time Complexity: O(n)
👉 We traverse the array once.

✅ Space Complexity: O(1)
👉 Only two variables are used regardless of input size.
"""
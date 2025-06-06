# 122. Best Time to Buy and Sell Stock II (Medium) - Done
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Returns the maximum profit by summing all positive differences
        between consecutive days where a price increase occurs.
        """

        profit = 0

        # Traverse prices starting from day 1
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


"""
✅ Time Complexity: O(n)
👉 Single pass through the array.

✅ Space Complexity: O(1)
👉 Uses only a profit accumulator.
"""

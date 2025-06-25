# 322. Coin Change (Medium) - Done
# https://leetcode.com/problems/coin-change


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Start with a large number (amount+1 is effectively "infinity" here)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


"""
✅ Time Complexity (TC):
O(amount × n)

Where:
amount is the total amount we want to make,
n is the number of different coin denominations.

Explanation:
You loop from 1 to amount → amount iterations.
For each amount, you iterate through all coins → n iterations.
So total operations = amount * n.

✅ Space Complexity (SC):
O(amount)

Explanation:
You use a 1D dp array of size amount + 1 to store the minimum coins required for each value from 0 to amount.
"""
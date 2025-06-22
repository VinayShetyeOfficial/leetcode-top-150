# 322. Coin Change (Medium)
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

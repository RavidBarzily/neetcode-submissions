class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            min_count = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    min_count = min(min_count, dp[i - coin] + 1)
            dp[i] = min_count
        return dp[-1] if dp[-1] != float('inf') else -1

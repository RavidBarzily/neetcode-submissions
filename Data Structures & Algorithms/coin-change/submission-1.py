class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1,amount + 1):
            min_val = float('INF')
            for coin in coins:
                if i >= coin:
                    min_val = min(min_val,dp[i - coin] + 1)
                dp[i] = min_val = min_val 

        if dp[amount] == float('INF'):
            return -1
        return dp[amount] 
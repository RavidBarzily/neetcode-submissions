class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        sol = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            max_val = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    max_val = max(max_val, dp[j] + 1)
            dp[i] = max_val
            sol = max(sol, dp[i])

        return sol
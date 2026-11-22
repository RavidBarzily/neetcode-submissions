class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = sol = float('-INF')
        for num in nums:
            curr = max(curr + num, num)
            sol = max(sol, curr)
        return sol
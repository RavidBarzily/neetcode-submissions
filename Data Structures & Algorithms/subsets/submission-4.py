class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        curr = []
        def dfs(i):
            if i >= len(nums):
                sol.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            dfs(i + 1,)

        dfs(0)
        return sol
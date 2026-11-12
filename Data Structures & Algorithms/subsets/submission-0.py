class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def helper(curr,i):
            if i == len(nums):
                return sol.append(curr.copy())
            curr.append(nums[i])
            helper(curr,i + 1)
            curr.pop()
            helper(curr,i + 1)
        helper([],0)
        return sol
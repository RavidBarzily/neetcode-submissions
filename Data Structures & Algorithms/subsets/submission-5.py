class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        for num in nums:
            sol += [ s + [num] for s in sol]
        return sol
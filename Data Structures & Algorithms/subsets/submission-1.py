class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        
        def helper(curr,i):
            if i  == len(nums):
                sol.append(curr.copy())
                return curr
            curr.append(nums[i])
            helper(curr,i + 1)
            curr.pop()
            helper(curr,i + 1)
            
        helper([],0)

        return sol
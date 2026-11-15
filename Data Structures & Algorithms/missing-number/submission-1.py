class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0

        for i in range(len(nums) + 1):
            curr += i
        
        return curr - total
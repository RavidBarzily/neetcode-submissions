class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0] * (n + 1)
        
        for i in range(1, n + 1):
            sol[i] = sol[i & (i - 1)] + 1
            
        return sol
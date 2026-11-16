class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = [0] * (n + 1)
        
        for i in range (1, n + 1):
            sol[i] = i % 2 + sol[i // 2]
        
        return sol
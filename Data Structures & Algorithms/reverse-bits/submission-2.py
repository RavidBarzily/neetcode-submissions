class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        for _ in range(32):
            sol <<= 1
            sol |= (n & 1)
            n >>= 1
        return sol
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles, h, k):
            hours = 0
            for pile in piles:
                hours += (pile + k -1)//k
            return hours <= h

        low,high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if can_finish(piles,h,mid):
                high = mid
            else:
                low = mid + 1
        return low
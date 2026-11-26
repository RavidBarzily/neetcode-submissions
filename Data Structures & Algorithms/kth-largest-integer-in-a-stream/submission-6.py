import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for num in nums:
            if len(self.h) != self.k:
                heapq.heappush(self.h, num)

            elif self.h[0] <= num:
                heapq.heappop(self.h)
                heapq.heappush(self.h, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]

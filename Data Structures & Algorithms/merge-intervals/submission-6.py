class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        sol = []
        for start, end in intervals:
            if not sol or sol[-1][1] < start:
                sol.append([start, end])
            else:
                sol[-1][1] = max(end, sol[-1][1])
        
        return sol
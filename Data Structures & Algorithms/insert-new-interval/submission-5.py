class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = list()
        after = list()
        for interval in intervals:
            if interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                newInterval = [min(interval[0], newInterval[0]),max(interval[1], newInterval[1])]
            elif interval[1] < newInterval[0]:
                before.append(interval)
            elif newInterval[1] < interval[0]:
                after.append(interval)
        before.append(newInterval)
        return before + after
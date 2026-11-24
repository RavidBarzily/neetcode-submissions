"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(intervals, key = lambda x: x.start)
        ends = sorted(intervals, key = lambda x: x.end)
        sol = count = i = j = 0
        while i < len(intervals) and j < len(intervals):
            if starts[i].start < ends[j].end:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            sol = max(sol, count)
        
        return sol
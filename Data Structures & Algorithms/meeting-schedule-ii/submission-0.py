"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = list()
        for i in range(len(intervals)):
            events.append((intervals[i].start, 1))
            events.append((intervals[i].end, -1))
        
        events.sort()
        sol = count = 0
        for _, b in events:
            count += b
            sol = max(sol, count)
        
        return sol
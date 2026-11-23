"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        print(list(zip(intervals, intervals[1:])))
        for a, b in zip(intervals, intervals[1:]):
            if a.end > b.start:
                return False
        return True
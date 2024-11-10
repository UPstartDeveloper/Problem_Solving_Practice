class Interval:
    """Definition of Interval:"""
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def get_times(self):
        """Shorthand for the start and end time"""
        return self.start, self.end


class Solution:
    """Source: https://neetcode.io/problems/meeting-schedule"""
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        """
        Intuition:
            search/sorting

        Constraints
            given: matrix of size (n, 2)
            intervals is immutable
            assume each start time < end time
            assume intervals fits in memory
            for now - assume each start time < next start time

        Edge Cases
            if n == 0 ---> return true
            overlapping start and end time --> not a conflict

        Approach

            1) Human Approach - 2 pters + fail fast
                A: compare each pair of adj intervals

                B: check start times are sorted AND check end_time1 <= start_time2
                    i: if not --> return false

                C: after full search --> return True
        """
        ### SPECIAL CASES
        if len(intervals) < 2:
            return True

        ### DRIVER
        index = 0
        intervals.sort(key=lambda interval: interval.start)

        while index < len(intervals) - 1:

            interval1, interval2 = intervals[index], intervals[index + 1]
            start_time1, end_time1 = interval1.get_times()
            start_time2, _ = interval2.get_times()

            if not (start_time1 < end_time1 <= start_time2):
                return False

            index += 1

        return True

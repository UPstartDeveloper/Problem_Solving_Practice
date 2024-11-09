class Solution:
    """From NeetCode"""
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Intuition:
            search + sorting problem

            merging func:
                given interval1, interval2

                if interval2_start <= interval1_end <= interval2_end:
                    merged_interval = [interval1_start, interval2_end]

        Constraints:
            given a matrix of shape nx2
            intervals is mutable
            n CAN be 0 ---> if so, return []
            interval times are int timestamps - all positive, 0-1000
            intervals - starts out, no merges needed
            assume newInterval sorted already

        Approach:



            1. human computer, not worrying about time optimization yet

                BEGIN: check special cases
                    - if newInterval should cleanly go at beginning
                    - OR if newInterval fits cleanly at the very last spot

                A: iter8 the list of intervals w/ 2 pters

                    for each current_interval, next_interval
                        check if it should be merged w/ newInterval
                            if so --> created merged_interval
                                replace the current_interval w/ the merged_interval in the list
                                exit early
                        check if (current_interval_end < newInterval_start) AND (newInterval_end < next_interval_start):
                            if so --> insert newInterval between them

                B: scan the list again - double check if any other merges needed

                C: return modified intervals

        """
        ### HELPER(S)
        def _get_merged_interval(interval1, interval2) -> list[int]:
            return [
                min(interval1[0], interval2[0]),
                max(interval1[1], interval2[1]),
            ]

        ### DRIVER
        ni = new_interval

        # check special cases
        if len(intervals) == 0:
            return [ni]

        elif ni[1] < intervals[0][0]:
            intervals.insert(0, ni)  # TODO[optimize]
            return intervals

        elif ni[0] > intervals[-1][1]:
            intervals.append(ni)
            return intervals

        # do human approach

        # A: iter8 the list of intervals w/ 2 pters
        if len(intervals) == 1:
            intervals.append(ni)
            intervals.sort(key=lambda x: x[0])
        else:
            index = 0

            # for each current_interval, next_interval
            while index < len(intervals) - 1:
                current_interval = intervals[index]
                next_interval = intervals[index + 1]

                # check if current_interval should be merged w/ newInterval
                if ni[0] <= current_interval[1]:
                    # if so --> created merged_interval
                    merged = _get_merged_interval(current_interval, ni)
                    # replace the current_interval w/ the merged_interval in the list
                    intervals[index] = merged
                    # exit
                    break

                elif (current_interval[1] < ni[0]) and (ni[1] < next_interval[0]):
                    # if so --> insert newInterval between them
                    intervals.insert(index + 1, ni)  # pushes next_interval further right

                index += 1

        # B: scan the list 1 more time - double check if any other merges needed
        index = 0
        while index < len(intervals) - 1:
            current_interval = intervals[index]
            next_interval = ni = intervals[index + 1]

            # check if current_interval should be merged w/ newInterval
            if ni[0] <= current_interval[1]:
                # if so --> created merged_interval
                merged = _get_merged_interval(current_interval, ni)
                # replace the current_interval w/ the merged_interval in the list
                intervals[index] = merged
                intervals.pop(index + 1)
            else:
                index += 1

        # C: return modified intervals
        return intervals

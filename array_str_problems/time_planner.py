def meeting_planner(slotsA, slotsB, dur):
    """
    input:  slotsA = [[10, 50], [60, 120], [140, 210]]
                            ^
            slotsB = [[0, 15],  [20, 50],[60, 70]]
                                ^
            
            dur = 8
            
    output: [60, 68]
    
    Intuitition: timelines


    0-------15       60----70
    B 0------------------------------------------------>
            10----50    60-------120    140-------210
    A 0------------------------------------------------>
    
    -
    
    Approach:
    ===============

    iterate over both 
    - take 2 intervals
        - try and find a meetig - if [x, y] return early
    - else:
        - keep iterating
        - find the greater of the two end times (in the current A and B)
        - for the other person, find the next start time
            - if next_st > larger endt
            - move the other index ahead


    - try and find meeting between 2 intervals:
            [0, 15], [10, 50], dur = 8
        - find the greater of the two start times
        - starting time + dur
        - check if that ending time works for both
            - if it does, return both those [10, 18]
            - else - return empty []


    ========================= Quadratic =================
    
    meeting_times = []
    
    time = 0
    
    iterating over person B's time - whoever has less avaliable spots
    
        find overlap with the other person
        - if there is an overlap
            - try and find time - if [x, y] return early
        - else:
            - keep iterating
        
        
        - how to tell if two meeting intervals overlap:
            -int1 = [0, 15]
                    11, 15
                    11, 70
            - int2 = [10, 50] 
                    
            if start_time2 < end_time1 < end_time2:
            - True
            elif  if start_time2 < start1 < end_time2:
            - True
            else
            return False
            
        - try and find meeting between 2 intervals:
            [0, 15], [10, 50], dur = 8
        - find the greater of the two start times
        - starting time + dur
        - check if that ending time works for both
            - if it does, return both those [10, 18]
            - else - return empty []
        
    
    Brute Force:
    find the largest time value
    iterate from 0 -> largest - dur
        - see if the [start, start + dur] works for both
        
        
    helper
    fits(schedule, meeting)
        if start_time2 < end_time1 < end_time2:
            - True
            elif  if start_time2 < start1 < end_time2:
            - True
            else
            return False
    """ 
    def find_next_intervals(index1, index2):
        start1, end1 = slotsA[index1]
        start2, end2 = slotsB[index2]
        # for the other person, find the next start time (move index ahead)
        if end2 > end1 and index1 < len(slotsA):
            index1 += 1
            if index1 < len(slotsA):  # not the end of the line
                start1 = slotsA[index1][0]
                # if next_st > larger end time
                if start1 > end2:
                    # move the other index ahead
                    index2 += 1
        elif index2 < len(slotsB):  # end2 <= end1
            index2 += 1
            if index2 < len(slotsB):  # not the end of the line
                start2 = slotsB[index1][0]
                # if next_st > larger end time
                if start2 > end1:
                    # move the other index ahead
                    index1 += 1
        return index1, index2
  
    def have_overlap(interval1, interval2, dur):
        """
        Determines if two time intervals have any overlap
        If so we return a suggested time interval
        """
        # unpack to get the start times and end times
        start1, end1 = interval1
        start2, end2 = interval2
        # see if the first one has any overlap w/ second
        meeting_times = list()
        if start2 < end1 <= end2:
            # go from the end time backwards
            start = end1 - dur
            if start >= start2 and end1 - dur >= start1:
                meeting_times = [start, end1]
        elif start2 <= start1 < end2:
            # go from start time forwards
            end = start1 + dur
            if end <= end1 and end <= end2:
                meeting_times = [start1, end]
        # otherwise there is no overlap
        return meeting_times
  
    # A: iterate over both schedules
    index1, index2 = 0, 0
    # B: find where the meeting can occur
    meeting = list()
    while index1 < len(slotsA) and index2 < len(slotsB):
        interval1, interval2 = slotsA[index1], slotsB[index2]
        # find if there's a meeting in the next two intervals for A and B
        meeting = have_overlap(interval1, interval2, dur)
        # if so, return it
        if len(meeting) == 2:
            return meeting
        elif len(have_overlap(interval2, interval1, dur)) == 2:
            return have_overlap(interval2, interval1, dur)
        # if not find the indices for the next iteration
        index1, index2 = find_next_intervals(index1, index2)
    # return the lack of a meeting
    return meeting  

    
    """ 
    def find_earlier_end(slotsA, slotsB):
        # find both ending times
        A_end, B_end = slotsA[-1][1], slotsB[-1][1]
        # return the smaller of the two
        earlier = A_end
        if B_end < A_end:
            earlier = B_end
        return earlier
    
    def find_later_start(slotsA, slotsB):
        # find both ending times
        A_start, B_start = slotsA[0][0], slotsB[0][0]
        # return the smaller of the two
        later = A_start
        if B_start > A_start:
            later = B_start
        return later
    
    def fits(slots, suggested_meeting):
        '''see if the suggested time overlaps with any of the slots'''
        suggested_start, suggested_end = suggested_meeting
        for slot in slots:
            slot_start, slot_end = slot
            if suggested_start >= slot_start and suggested_end <= slot_end:
                return True
        return False
    
    # A: find the bounds on the times
    start, end = (
        find_later_start(slotsA, slotsB),
        find_earlier_end(slotsA, slotsB)
    )
    # iterate to find the meeting time
    meeting = list()
    for time in range(start, end + 1):
        # see if the [start, start + dur] works for both
        meeting = [time, time + dur]
        if fits(slotsA, meeting) is True and fits(slotsB, meeting) is True:
            return meeting
    return []
    """
    """
      input:  slotsA = [[10, 50], [60, 120], [140, 210]]
                          ^
              slotsB = [[0, 15],  [20, 50],[60, 70]]
    Helper Functions:
    1. If a suggested interval fits within a second
    2. See if there's any overlap between two intervals
        if start_time2 < end_time1 <= end_time2:
            - True --> go from the end time backwards
            elif  if start_time2 <= start1 < end_time2:
            - True --> go from start time forwards
            else
            return False ===> return empty list
    3. iterate over both schedules
        - take 2 intervals
        - try and find a meetig - if [x, y] return early
    - else:
        - keep iterating
        - find the greater of the two end times (in the current A and B)
        - for the other person, find the next start time
            - if next_st > larger endt
            - move the other index ahead
    """

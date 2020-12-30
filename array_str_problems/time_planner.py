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

from typing import List


class Solution:
    """
    LeetCode: https://leetcode.com/problems/queue-reconstruction-by-height/
    
    Rachit Tayal's Appraoch: 
      sort the people based on height, in increasing fashion.
      if height are same, person with more taller people in front should be aligned first

      the index for shortest person = # of people taller in front of him + # of shorter people in front of him + 1
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # A: init queue
        queue = [-1 for p in people]
        # B: sort people based on height (and how far right they will be, f they have equal height)
        people.sort(key=lambda p: (p[0], -p[1]))
        # C: settle people's positions
        for person in people:
            taller_in_front = person[1]
            for index, pos in enumerate(queue):
                # check for shorter ppl in front-see if the pos is open
                if taller_in_front == 0 and queue[index] == -1:
                    # this position belongs to person
                    queue[index] = person
                    break
                # this spot is "reserved" for someone else - move on
                elif pos == -1 and taller_in_front > 0:
                    taller_in_front -= 1
        # D: all done
        return queue

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Input/Problem:
            2 arrays ----> of 1D lists ---> int intervals
            1 can be empty
            interval ---> non-neg ints, first < second
            in one input ----> disjoint (no overlaps IN a list)
            immutable
            
        Output:
            return a new list of OVERLAP intervals btween the 2 lists
            
        Intuition:
            set theory 
            number line
            
        A.        --------              ---
        B               ----                    ---
                                                                    max
            0 ----------------------------------------------------> 
                        3.5
                        
        EC: 
            1) 1 input list emmpty ----> []
            2) range of 1 list --? really far off from other ---> []
            3) TODO
            
        Approach:
            
            1) Brute Force - Array as Number Line
            
                1 = both in A and B
                0 = other

                [           1, 1 1                  00000000000000000000000    ]
                0           3 4. 5                                           26

                [[3, 5]]
                
            2) Stepping Stone: find 1 intersection
            
            [0, 2] 
            [1, 5]
            
            max(start), min(end) ----> [1, 2]
            
            3) Full Solution: 2 pointers
                firstList = [[0,2],[5,10],[13,23],[24,25]],
                                                           ^
                secondList= [[1,5],[8,12],[15,24],[25,26]]
                                                            ^
                output = [[1, 2], [5, 5], [8, 10], [24, 24]]
            
            A: init output list
            B: 2 pointer --> find all intersection (while loop)
                a: if no overlap --> move ahead both pointers
                b: if overlap --> add to output (max(start), min(end))
                    move ahead:
                    a: if both pointers at end - move both ahead
                    b: if 1 pointer is at end of its list already - move other poter
                    c: if next interval: pt'er in the ls w/ < start (in next interval)
            C: return output

        """
        ### HELPERS
        def _calculate_overlap(interval1, interval2):   # [1, 2] [10, 20]
            """max(start), min(end) --> if no overlap, return []"""
            start1, start2 = interval1[0], interval2[0]
            end1, end2 = interval1[1], interval2[1]
            guess = [max(start1, start2), min(end1, end2)]   # 10, 2
            if guess[0] <= guess[1]:  # validation
                return guess
            return list()  # not actually an overlap
        
        def _find_intersections(fL, sL):
            output, index1, index2 = list(), 0, 0
            while index1 < len(fL) and index2 < len(sL):
                interval1, interval2 = fL[index1], sL[index2]
                # a: calc overlap, add to output (max(start), min(end))
                overlap = _calculate_overlap(interval1, interval2)
                if len(overlap) > 0:
                    output.append(overlap)
                # b: if next interval: pt'er in the ls w/ < start (in next interval)
                if index1 < len(fL) - 1 and index2 < len(sL) - 1:
                    next_start_1, next_start_2 = fL[index1 + 1][0], sL[index2 + 1][0] 
                    if next_start_1 <= next_start_2:
                        index1 += 1
                    elif next_start_2 <= next_start_1:
                        index2 += 1
                # c: if 1 pointer is at end of its list already - move other pter
                elif index1 == len(fL) - 1:
                    index2 += 1
                elif index2 == len(sL) - 1:
                    index1 += 1
                # d: in all other cases - move both ahead
                else:
                    index1 += 1; index2 += 1
            return output

        ### DRIVER
        # A: 2 pointers --> find all intersection (while loop)
        output = _find_intersections(firstList, secondList)
        # B: return output
        return output

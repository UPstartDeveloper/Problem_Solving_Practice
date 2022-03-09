from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        LeetCode: https://leetcode.com/problems/remove-covered-intervals/
        
        Input:
        
                a ---------------------b
            c---------------------d
        
        <------------------------------------------->
        
        int[non empty ][2, non-neg, overlapping, immutable]
        random order
        

        Output:
            # of intervals after redunants taken out
            
        Intuition:
            graphs
            hashmap
            
        EC:
            ordering matters?
            
        Approach:
        
            A: brute force:
                1) init a hashset/2D list
                2) traverse the intervals
                    a) place in an existing set
                        get min of starts/maxes of ends
                    b) start a new group
                3) return length of 2D list
                
            Time: 
                let i = # of intervals
                O(i log i) + O(i^2) --> O(i^2)
            Space:
                O(i)
                
       [[1,4],[3,6],[2,8]]
       
       [
            [1, 4],
            [3, 6]
       ]
            
        
        """
        ### MAIN
        intervals.sort(reverse=True, key=lambda x: x[1] - x[0])
        # 1) init a hashset/2D list
        groups = list()
        # 2) traverse the intervals
        for interval in intervals:
            # a) place in an existing set
            for index, g in enumerate(groups):
                start_g, end_g = g
                start_i, end_i = interval
                # get min of starts/maxes of ends
                bounds = [
                    min(start_g, start_i),
                    max(end_g, end_i)
                ]
                print("comparing", g, interval, bounds)
                # place the larger interval in groups
                if bounds == interval or bounds == g:
                    groups[index] = bounds
                    break
            # b) start a new group
            else:
                groups.append(interval)
        # 3) return length of 2D list
        return len(groups)
        
       
    
"""
groups = [
    [1, 4],    < -- group
    [3, 6],
    
]

intervals = [
    [1, 4],     
    [3, 6],    < -- interval
    [2, 8]
]

sg = 3
se = 6
si = 1, 
ei = 4

bounds = [1, 6]

"""
        

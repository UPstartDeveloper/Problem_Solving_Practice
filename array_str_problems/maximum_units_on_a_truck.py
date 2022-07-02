from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        LeetCode: https://leetcode.com/problems/maximum-units-on-a-truck/
        
        Input:
            int[][].len > 1
            pos int
            unsorted
            dupes? I guess so
            immutable
            
            we CAN add partial
            we can mix
            
        Output: 
            max(# units)
                = sum(# box_type_1 * units_per_box_1 + )
            
        Intuition:
            constrained maximization
            sorting - max heap, sorting, greedy
            
        EC:
            empty arr --> 0
            truckSize < 0 ---> ValueError
            
        Approach:
        
            1) DIY - try to get as many of "dense" boxes first - O(n log n)
                
                A: sort by greatest to least # units/box
                B: greedy - add boxes into truck
                
                C: compute final weight
                
        """
        ### HELPERS
        def _add_boxes(sorted_bt):
            added_total = 0
            total_weight = 0
            
            # add boxes while we can
            for index in range(len(sorted_bt)):
                boxes_left, _ = sorted_bt[index]
                # add box w/ constraint
                added = min(boxes_left, truckSize - added_total)
                added_so_far += added
                # update truck weight (in total)
                total_weight += sorted_bt[index][1] * added           
                
            return total_weight
        
        ### GUARD clauses
        # TODO
        ...
        
        ### DRIVER - assume valid input
        # A:
        bt = boxTypes
        bt.sort(reverse=True, key=lambda pair: pair[1])
        
        # B: 
        total_weight = _add_boxes(bt)
        
        return total_weight

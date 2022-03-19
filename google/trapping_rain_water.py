from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Input:
            - int[>=0, non-empty, unsorted, dupes]
            
        Stepping Stones:
            - Trap Detection
                left  >  mid_height < right_side
                height = a sequence of the same unique value
                (hint: expand right_side while we have elem < left)
                represent trap = [global_left_ndx, global_right_ndx]
                
            - Compute the Volume of Water Trapped:
                - @each trap:
                    water_height = min(global_left, global_right)
                    @each pos in the seq (including boundaries):
                        volume += 
                            diff(water_height, pos_height) 
          
          
        EC:
        
            1) repeating values
            
                [0,1, 0,0,0,0,0,0,0, 1,2,1]
                
                0. 1. 2 3 4
            2) [4,2,0,3,2,5]
                l
                           r
                        p
            
           A: detect where all the traps are
           
           B: compute the volume, from each trap <-
           
           C: return total_volume of trapped water
           
           
           traps = [
                [0, 4]   <----- trap
           ]
           
           total_volume = 0, 2, 6, 7, 9
           
           water_height = 4
           
           pos = 0
                
        LeetCode: https://leetcode.com/problems/trapping-rain-water/
        """
        ### HELPERS
        def _find_traps(height):  # TODO[test]
            traps = list()
            # find traps
            index = 0
            while index < len(height) - 1:
                left_ndx, left = index, height[index]
                right_ndx = left_ndx + 1
                # (hint: expand right_side while we have elem < left)
                while right_ndx < len(height) and height[right_ndx] < left:
                    right_ndx += 1
                # represent trap, and move on
                if right_ndx < len(height):
                    traps.append([left_ndx, right_ndx])
                    index = right_ndx
                else:
                    index += 1
            return traps
        
        def _compute_trapped_vol(traps):
            vol = 0
            # @each trap:
            for left_ndx, right_ndx in traps:
                left_height, right_height = (
                    height[left_ndx], height[right_ndx]
                )
                water_height = min(left_height, right_height)
                # @each pos in the seq (including boundaries):
                for pos in range(left_ndx, right_ndx + 1):
                    pos_height = height[pos]
                    # acculmulate trapped water
                    if pos_height < water_height:
                        vol += water_height - pos_height
            return vol
        
        ### MAIN
        # A: scan left-right - get largest preceding heights
        lr_scan = [0 for _ in range(len(height))]
        max_h = height[0]
        for index in range(len(lr_scan)):
            ht = height[index]
            max_h = max(max_h, ht)
            lr_scan[index] = max_h
        # B: scann right-left - get largest succeeding ht's
        rl_scan = [0 for _ in range(len(height))]
        max_h = height[-1]
        for index in range(len(lr_scan) - 1, -1, -1):
            ht = height[index]
            max_h = max(max_h, ht)
            rl_scan[index] = max_h
        # C: "the overlap" = total vol of trapped water
        vol = 0
        for ht, left, right in zip(height, lr_scan, rl_scan):
            vol += min(left, right) - ht
        return vol
        

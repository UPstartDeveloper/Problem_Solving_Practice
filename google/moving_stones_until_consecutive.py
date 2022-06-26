from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/moving-stones-until-consecutive/

        Input: 3 unique pos ints < 101
                (unsorted, mutable)
                
        Output: 2-tuple
            min + max # of moves
            
        Intuition:
            logic
            math
            
        EC:
            invalid inputs (non-numeric) - ValueError
                            neg, 0, float - support Later
                            
        Approach:
        
            1) DIY
            
                a) sort a b c --> x < y < z - TODO[sorting-algo]
                
                b) solve for min # 
                    
                    moves = 0 OR 1 OR 2
                        0: both already adj ---> return 0
                        1: one is adj ----> return 1
                        2: neither already adj --> find optimal final positions,
                                                  then work backwards
                    
                c) solve for max #
                
                    moves = sum([
                        abs(y - x) - 1,
                        abs(z - x) - 1
                    ]), don't allow negatives
                
                d) done! return [min, max]
            
            2) a little better:
                plan: whichever endpt is farther, eval moving (pivot - 1, pivot + 1)
                
                A: min approach:
                
                    iterate: while not is_consecutive
                        measure dist1, dist2 (both endpts)
                        
                        if dist1 != dist2:
                            choose larger
                                eval both options (before/after mid)
                                move it to best one (if poss, else do other)
                                increment moves
                        
                        else if dist1 == dist2:
                        
                            if dist1 < 3:
                                return max(0, dist1 - 1)  # special case
                            
                            else:
                                choose the right endpt, do above
                        
                        return moves, final_positions
                        
                B: max approach:                
                    iterate: while not is_consecutive
                        measure dist1, dist2 (both endpts)
                        
                        if dist1 != dist2:
                            choose larger
                                eval both options (before/after mid)
                                move it to *worst* one (if poss, else do other)
                                increment moves
                        
                        else if dist1 == dist2:
                        
                            if dist1 < 3:
                                return max(0, dist1 - 1)  # special case
                            
                            else:
                                choose the right endpt, do above
                        
                        return moves, final_positions
                                                
        """
        ### HELPERS
        ...

        ### DRIVER
        a, b, c = sorted(list([a, b, c]))

        return list([_compute_min(a, b, c), _compute_max(a, b, c)])  # TODO  # TODO

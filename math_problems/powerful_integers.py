import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/powerful-integers
        
        Input:
            x, y --> bases, pos ints
            bound --> non neg ---> threshold
            
            powerful int
                sum(x**i, y**j) ---> i, j >= 0
                
        Output: set of ints <= b
        
        Intuition:
            math
        
        EC:
            - x or y is 1:
                should avoid using the log() function with any x > 1
            - bound < 2
                return []
            
        Approach:
        
            1. Brute force:
                A: init ints: 0 <= set <= bound
                B: check which can be found using sum(x**i, y**j)
                    - 0 and 1 are NEVER achievable
                    - 
                
                bound = 10
                
                {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
                    ^
        """
        ### HELPRS        
        def _get_closest_sq_root(x, base):
            if base == 1:
                return 1
            return math.floor(math.log(x, base))
        
        def _sum_set(x, y, bound):
            # A: get closest square roots of x y 
            x_root = _get_closest_sq_root(bound, x)
            y_root = _get_closest_sq_root(bound, y)
            # B: compute all their sums 
            sum_set = set()
            for x_exp in range(0, x_root + 1):
                for y_exp in range(0, y_root + 1):
                    # check if it falls in the range!
                    sum_val = sum([x ** x_exp, y ** y_exp])
                    if sum_val <= bound:
                        sum_set.add(sum_val)
                
            # return answers
            return list(sum_set)
        
        ### MAIN
        # Edge Cases:
        if bound < 2:
            return list()
        return _sum_set(x, y, bound)

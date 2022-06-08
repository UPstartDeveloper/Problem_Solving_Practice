import math
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/counting-bits/
        
        Input:
            n - non neg int
            immutable
            
        Output:
            arr - map index --> count(bin(index), 1)
            
        Intuition:
            bit manipulation
            DP 
        
        EC:
            n -> not int or n < 0 ---> ValueError

        Approach:
            
            1) Brute force
                ans = []
                traverse 0 --> n  
                    for each val --> binary rep  O(log n)
                    count # of 1's
                    ans += count
                return ans
                
            2) Brute Force and memoize
                
            3) Rules
                0 ---> 0
                power of 2 ---> 1
                in-between values ---->
                    ans[last power of 2] + ans[remaining]
            
            log2(i) --> bound on # 1's 
            log2(0) --> N/A 
            log2(1) --> 0
            log2(2) --> 1
        """
        
        ### HELPERS
        def _get_powers_in_range(n): 
            # list out powers of 2 (start at 1) while <= n
            max_exp = int(math.log2(n))
            powers_of_2 = set([
                2 ** exp for exp in range(0, max_exp + 1)
            ])
            return powers_of_2
        
        def _set_in_between_values(a, powers_of_two):            
            last_power_2 = lp2 = 1 
            # traverse 3 --> n using i:
            for index in range(1, n + 1):
                # base case - check if i is a power of 2
                if index in powers_of_two:
                    a[index] = 1
                    lp2 = index
                # recursive case
                else:  
                    remaining = r = index - lp2
                    # ans[last power of 2] + ans[remaining]
                    a[index] = a[lp2] + a[r]
        
        ### DRIVERS
        if isinstance(n, int) is False or n < 0:
            raise ValueError(f"Expected a non-negative int for 'n', received: {n}") 
        if n == 0:  # extra edge case
            return [0]
        
        # start w/ all powers of 2
        answers = a = [0 for _ in range(n + 1)]
        powers_of_two = _get_powers_in_range(n)  # O(log n)
        
        # populate the rest - the "in-between values"
        _set_in_between_values(a, powers_of_two)
        
        return a

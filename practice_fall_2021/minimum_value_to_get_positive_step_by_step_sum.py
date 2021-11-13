from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
        
        Input/Problem:
            - non empty int arr
            - immutable
            - pos/neg
            - dupes
            
        Output:
        
            int > 0
            min value 
            
        Intuition
            startValue + sum(nums) >= 1
            
            step-by-step ===> decrease w/ neg number
            
        EC:
            1) pos values ---> 1
            2) empty arr
            3) value outside range
            4) TODO
            
        Approach:
        
            1. Brute Force: ---> O(n * k)
                A: check all pos nums, (>= 1)
                B: check if it's a valid startValue
                    C: if true, return that pos num
                
            2. Optimal Approach:
            
                A: 1 or 2 passes - "guess" sV
                    B: 1 + abs(min(nums)) -----> if the min < 0
                    C: min(nums) ---> is min is pos
                D: check the guess -- is_valid
                    E: in case it's not valid, return 1 + guess
            
            3. Optimal Approach
            
                A: startValue = 0
                    B: see the sss at each iteration - see min
                    C: guess abs(min), if min < 0
                    D: if min >= 0, return 1
                E: is_valid(guees)
                    
                    
                [1,-2,-2,-2,-2,-2,-3]
                
        
        
        """
        ### HELPERS
        def _make_guess():
            sum_so_far = ssf = 0
            min_val = float("inf")
            for num in nums:
                ssf += num
                if ssf < min_val:
                    min_val = ssf
            # make guess
            if min_val < 0:
                return abs(min_val) + 1
            else:
                return 1
        
        ### DRIVER
        return _make_guess()
        
    

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/maximum-product-subarray/
        
        Input:
            int[immutable, pos/neg, dupes, sorted]
            
        Output:
            max(prod(sub))
            len(sub) > 0
            
        Intuition:
            Dynamic programming
            
        EC:
            - all postivies --> prod(nums)
            - TODO
            
        Approach:
        
            1. Brute:
                all sub arrs
                  4: [2, 3, -2, 4]
                  3: [2, 3, -2,], [3, -2, 4]
                  ...
                  2: [2, 3]
                  1: [2,], [3],
                max(products)
              
prefix_prods 2. 6. -12  48
                 .  s   l
            [2, 3, -2, -4]
            [2] ----> 2
            2.  6   -12 -48
                l      s
            [2, 3, -2, 4]
            
            -2   0    -1
             s   l   
            [-2, 0, -1]
    rp       -2.     1        
        # A: running_prod = rp = 1
        
        # B: index = 0
        
        # C: find the largest/smallest ===> 0
            largest_prodct = float("-inf")
            largest_index = 0
            smallest_product = float("inf")
            smallest_index = 0
            
            a) loop through the arr
            
            b) update rp with current elem
            
            c) rp > largest
                largest_index ---> index
            d) rp < smallest ---> index
                smallest_index ---> index
                
            e) if elem == 0: rp = 1
        
        # D: return largest_prodct
        
        """
        ### HELPERS
        def _find_largest_smallest(mode):
            # A: init vars 
            running_prod = rp = 1
            largest_product = float("-inf")
            smallest_product = float("inf")
            
            # B: loop through the arr --> find the largest/smallest ===> 
            if mode == "forward":
                start, stop, change = 0, len(nums), 1
            else:  # mode == "backward"
                start, stop, change = len(nums) - 1, -1, -1
            for index in range(start, stop, change):
                
                elem = nums[index]
                # a) update rp with current elem
                if elem == 0:
                    rp = 0
                else:
                    rp *= elem
                    
                # b) update l/s
                largest_product = max(rp, largest_product)
                smallest_product = min(rp, smallest_product)

                if elem == 0:
                    rp = 1
            
            # all done!
            return largest_product
        
        
        ### MAIN
        # A: find prefix and suffix prods 
        largest_product_fwd = _find_largest_smallest("forward")
        largest_product_back = _find_largest_smallest("backward")
        # B: all done!
        return max(largest_product_fwd, largest_product_back)
        

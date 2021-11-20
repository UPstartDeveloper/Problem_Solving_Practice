from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/single-element-in-a-sorted-array/
        
        Input:
            non empty non-neg int[]
            assume immutable
            sorted
            dist:
                all but 1 ----> x2
            size: always odd
            
        Output: ---> 1 elem x 1
        
        Intuition:
            binary search
            bitwise
            
        EC:
            1. invalid inputs ---> ValueError
                []
                num < 0
            2. even # of elems ---> ASSUME not going ot happen
                [1, 2]
            3. TODO
            
        Approaches:
        
            Linear time solution:
                1. Linear search w/ 2 pters
                2. XOR over 
                3. HashTable ---> hist ogf nums ---> binary search for the elem x1
                
            DSBS: "leapfrog"
                2 pointers ---> n / 2
                         m
                [1,1,2,3,3,4,4,8,8]
                     ^
                       ^

                 [3,3,7,7,10,11,11]
                           ^ ^
                           
                          v     
                [3,3,7,7,10,11,11]
                
                odd # of elems
                
               [   odd/even #, m, odd/even # ]
                
        
                
                if 
        Modified B-Search:
        
        Base case: answer is found ---> both L and R are diff
        Recursive case: go left
            left num == middle AND even # of elems on left OR
            left num != middle ANND odd # of elems on left
        else (Recursive) case: go right
                       
        
        """
        ### HELPERS
        def _search_linear(nums):
            # A1: check each pair, stop when the single number is found
            index1, index2 = 0, 1
            while index2 < len(nums) and nums[index1] == nums[index2]:
                index1 += 2; index2 += 2
            return nums[index1]
        
        def _search_binary(nums):
            
            def _get_lr(mid_ndx):
                left, right = None, None
                if mid_ndx > 0:
                    left = nums[mid_ndx - 1]
                if mid_ndx < len(nums) - 1:
                    right = nums[mid_ndx + 1]
                return left, right
            
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                # get middle
                mid_ndx = (lo + hi) // 2
                mid_elem = nums[mid_ndx]
                # get left and right if poss
                left, right = _get_lr(mid_ndx)
                # Base case: answer is found ---> both L and R are diff
                if (
                    (left and right and left != mid_elem and mid_elem != right) or 
                    (mid_ndx == 0 and mid_elem != right) or
                    (mid_ndx == len(nums) - 1 and mid_elem != left)
                ):
                    break
                # Recursive case: on left side
                if left and mid_elem == left:
                    if mid_ndx % 2 == 0:  # should be odd
                        hi = mid_ndx - 1
                    else:
                        lo = mid_ndx + 1
                elif right and mid_elem == right:   # on right side
                    if mid_ndx % 2 == 0:  # go right should be even
                        lo = mid_ndx + 1
                    else:
                        hi = mid_ndx - 1 # go right, b/c should be even
            # target found
            return nums[mid_ndx]
        
        ### DRIVER
        return _search_binary(nums)
        
        

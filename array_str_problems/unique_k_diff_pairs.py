from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Leetcode: https://leetcode.com/problems/k-diff-pairs-in-an-array
        
        Input/Problem:
            nums = int[dupes, unsorted, pos/neg, non-empty]
            k - nonneg
            elem --> can be in more than 1 pair
                 --> IN a single pair --> only use 1x
            
        Output:
            # of unqiue 
                (1, 3) == (3, 1)
                
        Intuition:
            heaps
            sorting
        
        EC: TODO
            - []--
            
        Approach:
            
            1. Nested for loops (quadratic, linear)
                - save the pair in a set - return len()
                
            2. Sorting the array --> O(nlogn) time, linear
                traverse the array
                    binary search for complements
                    
            3. HashSet --> O(n), O(n)
                    [1,3,1,5,5,5,4, 4,4,4], k = 0
                    {              #  pairs
                        1: 2,  ---> 1
                        3: 1, ----> 0
                        5: 3, ----> 1
                        4: 4 -----> 1
                    }
                if k > 0
                    cast nums ---> set()
                    iterate over nums
                        calculate the complement
                        look up in set
                else k == 0:
                    Counter(nums)
                    acculmulate 1 for each key-value where val > 1
                    
            
            
            [3, 1, 4, 1, 5], k = 2
                ^
                    ^ 
                
            (1, 3), (3, 5)
            
            num1 = 1
            k =    2
            
            complements = -1, 3
            
            [1,2,3,4,5]
             ^
        <--- k --->
        """
        ### HELPERS
        pass
    
        ### MAIN
        # A: init the output
        num_pairs = 0
        
        # B: count the pairs
        if k == 0:
            histogram = Counter(nums)
            for val, count in histogram.items():
                if count > 1:
                    num_pairs += 1
        else:  # k > 0
            pairs = set()
            # cast nums ---> set()
            nums_set = set(nums)
            for num in nums_set:
                # TODO[refacotr]
                # calculate the complement
                lower = num - k
                upper = num + k
                # look up in set
                if lower in nums_set:
                    pairs.add((lower, num))
                if upper in nums_set:
                    pairs.add((num, upper))
            num_pairs = len(pairs)
            
        # C: output
        return num_pairs

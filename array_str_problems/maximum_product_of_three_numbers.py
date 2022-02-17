from functools import reduce
from typing import List

class Solution:
    ### LeetCode: https://leetcode.com/problems/maximum-product-of-three-numbers
    def maximumProduct(self, nums: List[int]) -> int:
        ### HELPER
        def _count_negatives(nums):
            return len([n for n in nums if n < 0])
        
        def _find_lowest_2(nums):
            least = set()
            # D: find the top 3 highest
            for _ in range(2):
                lowest, lowest_index = float("inf"), -1
                for index, elem in enumerate(nums):
                    if elem < lowest and index not in least:
                        lowest = elem
                        lowest_index = index
                # save this index for later
                least.add(lowest_index)
            # E: return their product
            return reduce(multiply, [nums[ndx] for ndx in least])
                
        multiply = lambda x,y: x * y
        
        def find_highest_product(nums):
            highest = set()
            # A: find the top 3 highest
            for _ in range(3):
                largest, largest_index = float("-inf"), -1
                for index, elem in enumerate(nums):
                    if elem > largest and index not in highest:
                        largest = elem
                        largest_index = index
                # save this index for later
                highest.add(largest_index)
            # B: return their product
            return reduce(multiply, [nums[index] for index in highest])
            
        ### MAIN
        # A: check # of negatives
        num_negs = _count_negatives(nums)
        # B: do appropiate preprocessing
        prod_with_negs = float("-inf")
        if num_negs < len(nums):
            prod_with_negs = _find_lowest_2(nums) * max(nums)
        # C: get the highest products
        prod_no_negs = find_highest_product(nums)
        return max(prod_with_negs, prod_no_negs)
        

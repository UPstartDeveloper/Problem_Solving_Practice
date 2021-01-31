from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        - assuming the following:
            - positive and negative ints
            - duplicates possible
            - empty? --> assume not going to happen
            - multiple sub arrays with the same product
            
        Intuition
        - start the subarray at the first value
        - while the next value (and no IndexError) makes the product greater, 
            - include it
        - when we are done expanding the subarray, see if it's product is greater than
            the largest product seen so far
        Approach:
        - 1 while loop - updating the start index of each subarray
            - nested while loop
                - finds where the end of that subarray should be
                - updates the start variable
        Edge Cases:
        - empty array
        
        [2,3,-2,4]
        - start the subarray at the first value
        - while the next value (and no IndexError) makes the product greater, 
            - include it
        - when we are done expanding the subarray, see if it's product is greater than
            the largest product seen so far
        
        [-2,0,-1] --> don't need to know what subarray actually is
            
        """
        # edge case: empty array
        assert len(nums) > 0, "the array is invalid"
        # TODO: handle edge case where the values aren't all the same
        
        # TODO: decide if the answer is the whole array
        def has_even_negatives(nums):
            '''return true if the num of negatives is even (including)'''
            negatives = 0
            for num in nums:
                if num < 0:
                    negatives += 1
            return (negatives % 2 == 0)
        
        def whole_sum(nums):
            '''return product of all the values'''
            product = 1
            for num in nums:
                product = product * num
            return product 
        
        # - start the subarray at the first value
        if has_even_negatives(nums) and (0 not in nums):
            return whole_sum(nums)
        else:
            start = 0
            largest_prod = float('-inf')
            while start < len(nums):
                end = start
                prod = nums[start]
                # - while the next value (and no IndexError) makes the product greater,
                while end < len(nums) - 1 and prod * nums[end + 1] > prod:
                        # include it
                        end += 1
                        prod *= nums[end]
                # see if it's product is greater than the largest
                if prod > largest_prod:
                    largest_prod = prod
                # find the next product
                start = end + 1
            return largest_prod
    
    
"""
  0
[-2, 3, -4]


        0 1  2 3
Input: [2,3,-2,4]

s       lp      e       p       nf
2       6       1       6       -2
3       6       2       -2      4 
3       6       3       4   

Output: 6

Input: [0, 2]

s = 0
lp = -inf
e = 0
p = 0
nf = 2


Brute Force:
what is the max subarray for size x? (x for x in 1,2,...n = size of nums)

"""

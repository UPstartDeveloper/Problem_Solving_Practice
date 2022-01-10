from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/product-of-array-except-self/
        
        # Naive Approach
        
        Input:  [1,2,3,4]
                []
                
        Intution:
        - focus on the just the products of elements to the left
        [1,        1,        2,          6]
        1         1*1      1*1*2        1*1*2*3
        - focus on the just the products of elements to the right
        [24       12         4           1]
                            1*4
        [24       12.        8           6]    
        
        
        - 1 app
                0
        Input:  [1,2,3,4]
        output = 
        [1, 1, 2, 6]
        
        product = 1, 1, 2, 6
        index = 0, 1, 2, 3
        []  ==> []
        [5] ===> []
        """
        # make an array filled with left side ansers
        output = list()
        if len(nums) > 1:
            product = 1
            for index in range(len(nums)):
                output.append(product)
                product *= nums[index]
            # modify the array to account for the right side
            right = 1
            for index in range(len(output) - 1, -1, -1):
                output[index] *= right
                right *= nums[index]
        # bring it all together
        return output


# Time and space O(n)

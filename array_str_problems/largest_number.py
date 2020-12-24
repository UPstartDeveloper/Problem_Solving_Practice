"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"

"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Questions:
         am I allowed to use the built-in sorting algorithm? yes
         is the input mutable? yes
         
        Assumptions:
        always at least one integer
        all nonnegative
         
        # intutition: 
        we need to make the largest digits appear in the largest
        (aka the leftmost) place values in our return number
        
        "sort by the leftmost place values of 10 in descending order"
        
        # approach: 
        # A: convert the numbers to strings
        # B: sort those strings in reverse
        # C: combine the strings into one, representing the output number
        
        # edge cases
        what if there's a leading 0? assume it's not possible
        
        """
        def get_key(num):
            # divide by 10 until the quotient is less than 10
            quotient = num
            place_values = 1
            while quotient > 9:
                quotient /= 10
                place_values += 1
            # if the num is divisible by 10, subtract by place_values
            key = quotient
            if num % 10 == 0:
                key = quotient - place_values
            return key
        # A: convert the numbers to strings
        """nums = [
            str(num) for num in nums
        ]"""
        # B: sort those strings in reverse
        nums.sort(reverse=True, key=get_key)
        print(nums)
        nums = [
            str(num) for num in nums
        ]
        # C: combine the strings into one, representing the output number
        return ''.join(nums)
    

"""
Test Input:
Input: nums = [3,30,34,5,9]
Output: "9534330"

nums = ["3","30","34","5","9"]
nums = [
    "9", "5", "34", "30", "3"
]
output: "9534330"

# Error - we need to realize that sometimes shorter numbers go ahead of 
          longer numbers, if they are otherwise equal (maybe just a trailing 0)
"""
        
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
from typing import List


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

        def leftmost_digits(nums):
            """return an array sorted by order of leftmost digit"""
            # init the array of values and indices
            values_indices = list()
            # populate the array with the leftmost digit from nums
            place_values = 0
            for index, num in enumerate(nums):
                while num > 9:
                    num = num // 10
                    place_values += 1
                values_indices.append((num, index, place_values))
            # sort the array by those left nums
            values_indices.sort()
            return values_indices

        def sort_by_remainder(tuple1, tuple2):
            """modulo divide by 10 until the numbers can be sorted"""
            # unpack both tuples, get the real numbers using the index
            val1, index1, place_values1 = tuple1
            val2, index2, place_values2 = tuple2
            # convert to strings for the comparison
            num1, num2 = (str(nums[index1]), str(nums[index2]))
            # iterate to find the shorter string
            iterations = len(num1)
            if len(num2) < len(num1):
                iterations = len(num2)
            for index in range(iterations):
                digi1, digi2 = (num1[index], num2[index])
                # compare the integers
                if digi2 > digi1:
                    return tuple1, tuple2
                elif digi1 > digi2:
                    return tuple2, tuple1
            # if no winner, return the shorter as the first number
            if len(num1) == iterations:
                return tuple2, tuple1
            else:  # len(num2) == iterations
                return tuple1, tuple2
            """ get the next leftmost digit from the numbers to compare
            digi1 = num1 // (10 * place_values1)
            digi2 = num2 // (10 * place_values2)
            # choose the greater number based on the greater digit
        while place_values1 > 0 and place_values2 > 0 and digi1 == digi2:
                digi1 = num1 // (10 * place_values1)
                digi1 = num1 % divisor
                digi2 = num2 % divisor
            # if all the comparable digits are tried, go with the smaller
            # return the tuples"""
            """
            # modulo divide by 10 until one has a greater remainder
            num1 /= 10  
            num2 /= 10
            while num1 == num2:
                num1 %= 10
                num2 %= 10
            # return the tuples in sorted order
            if num1 <= num2:
                return (tuple2, tuple1)
            else:  # num2 turns out to be the value that comes first
                return (tuple1, tuple2)"""

        # A: find the leftmost number in each given integer
        # use it to make a new array (val, index)
        values_indices = leftmost_digits(nums)  # O(n(log n + log k))
        # B: take values from the (somewhat) sorted new array
        final = list()
        index = len(values_indices) - 1
        while index > -1:  # n iterations
            value, num_index = (values_indices[index][0], values_indices[index][1])
            if (
                len(values_indices) > 1
                and index > 0
                and value == values_indices[index - 1][0]
            ):
                # then sort them more
                values_indices[index - 1], values_indices[index] = sort_by_remainder(  #
                    values_indices[index - 1], values_indices[index]
                )
            # print(values_indices)
            # then add it to a final array
            num_index = values_indices[index][1]
            final.append(str(nums[num_index]))
            # and move on to adding the next number
            index -= 1
        # C: make the final number string
        return "".join(final)  # n iterations

        """
        def leftmost_digits(nums):
            '''return an array sorted by order of leftmost digit'''
            # init the array of values and indices
            values_indices = list()
            # populate the array with the leftmost digit from nums
            for index, num in enumerate(nums):
                while num > 9:
                    num = num // 10
                values_indices.append((num, index))
            # sort the array by those left nums
            values_indices.sort()
            return values_indices
            
        def sort_by_remainder(tuple1, tuple2):
            '''modulo divide by 10 until the numbers can be sorted'''
            # unpack both tuples, get the real numbers using the index
            val1, index1 = tuple1
            val2, index2 = tuple2
            num1, num2 = nums[index1], nums[index2]
            # modulo divide by 10 until one has a greater remainder
            num1 %= 10  
            num2 %= 10
            while num1 == num2:
                num1 %= 10
                num2 %= 10
            # return the tuples in sorted order
            if num1 <= num2:
                return (tuple2, tuple1)
            else:  # num2 turns out to be the value that comes first
                return (tuple1, tuple2)
        # A: find the leftmost number in each given integer
        # use it to make a new array (val, index)
        values_indices = leftmost_digits(nums)  # O(n(log n + log k))
        # B: take values from the (somewhat) sorted new array
        final = list()
        index = len(values_indices) - 1
        while index > -1:  # n iterations
            value, num_index = values_indices[index] 
            if len(values_indices) > 1 and index > 0 and value == values_indices[index - 1][0]:
                # then sort them more
                values_indices[index], values_indices[index - 1] = (
                    sort_by_remainder(  # 
                        values_indices[index], values_indices[index - 1]
                    )
                )
            # then add it to a final array
            num_index = values_indices[index][1]
            final.append(str(nums[num_index]))
            # and move on to adding the next number
            index -= 1
        # C: make the final number string
        return ''.join(final)  # n iterations
        """
        """
        def leftmost_digits(nums):
            '''return an array sorted by order of leftmost digit'''
            # init the array of values and indices
            values_indices = list()
            # populate the array with the leftmost digit from nums
            for index, num in enumerate(nums):
                while num > 9:
                    num /= 10
                values_indices.append((num, index))
            # sort the array by those left nums
            values_indices.sort()
            return values_indices
            
        def sort_by_remainder(tuple1, tuple2):
            '''modulo divide by 10 until the numbers can be sorted'''
            # unpack both tuples, get the real numbers using the index
            val1, index1 = tuple1
            val2, index2 = tuple2
            num1, num2 = nums[index1], nums[index2]
            # modulo divide by 10 until one has a greater remainder than the other
            num1 %= 10
            num2 %= 10
            while num1 == num2:
                num1 %= 10
                num2 %= 10
            # return the tuples in sorted order
            if num1 <= num2:
                return (tuple2, tuple1)
            else:  # num2 turns out to be the value that should come first
                return (tuple1, tuple2)
        # A: find the leftmost number in each given integer
        # use it to make a new array (val, index)
        values_indices = leftmost_digits(nums)
        # B: take values from the (somewhat) sorted new array - move backwards
        final = list()
        index = len(values_indices) - 1
        while index > -1:
        """
        """
        # if a value is uncontested
        value, num_index = values_indices[index] 
        if (index == 0) or (value != values_indices[index - 1][0]):
            # then add it to a final array
            final.append(str(nums[num_index]))
            # and move on to adding the next number
            index -= 1
        # if not
        else:  # value == values_indices[index - 1][0]
            # then sort them more
            values_indices[index], values_indices[index - 1] = (
                sort_by_remainder(
                    values_indices[index], values_indices[index - 1]
                )
            )
        
        value, num_index = values_indices[index] 
        if value == values_indices[index - 1][0]:
            # then sort them more
            values_indices[index], values_indices[index - 1] = (
                sort_by_remainder(
                    values_indices[index], values_indices[index - 1]
                )
            )
        # then add it to a final array
        final.append(str(nums[num_index]))
        # and move on to adding the next number
        index -= 1
        # C: make the final number string
        return ''.join(final)
        
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
        '''nums = [
            str(num) for num in nums
        ]'''
        # B: sort those strings in reverse
        nums.sort(reverse=True, key=get_key)
        print(nums)
        nums = [
            str(num) for num in nums
        ]
        # C: combine the strings into one, representing the output number
        return ''.join(nums)

        Test Input:
        Input: nums = [3,30,34,5,9]
        Output: "9534330"

        nums = ["3","30","34","5","9"]
        nums = [
            "9", "5", "34", "30", "3"
        ]
        output: "9534330"

        # Error - we need to realize that sometimes shorter numbers go ahead of 
        # longer numbers, if they are otherwise equal (maybe just a trailing 0)
"""

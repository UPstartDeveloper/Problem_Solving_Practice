"""
Ctci 5.3:

Flip Bit to Win: 

You have an integer and you can flip exactly one bit from a 0 to a 1.

Write code to find the length of the longest sequence of ls you could create.


EXAMPLE            12345678
Input: 1775 ( or : 1110111101111)
                       123456789

Output: 8

Clarifications:
1. What if there are muliple indices where we could flip 0 --> longest sequence?
    a. example input: 0000000000000
    a. fine, just return the length found

2. ASSUME only positive integers

Intuition:
1) multiple sequences of contiguous 1's 

Edge Cases:
1. all 1's ---> num of bits
2. all zeros --> return 1, special case it 
3. alternating zeroes and ones 
4. float? --> validate in the beginning, rasie ValueError

Approach (after special cases):

1. Brute Force:
    A: store bits in an array
    B: use 2 pointers
        i. init counters for ones, and max_ones
        ii. keep iterating over the bits until the end
        iii. back track

    0123456789012
    11101111011110
        ^               cb
       ^               zi
            ^               zn
    [3, 8, 13]
    13 - 4 = 9
    0 - 8 = 8

   ones = 0
   max_ones = 8
   current_bit = 0 --> 8 --> zero_included + 1 = 4
   zero_included = current_bit = 0 --> 3
   zero_not_included = zero_included = 3 --> 8

2. More Space:
    A: store bits in an array
    B: store locs of 0 bits in another array
    C: return the highest difference between locs in 2nd array

3. Brute Force, not as many pointers:
    A: store bits in array
    B: count consecutive ones, (includes first zero) up to 2nd zero
    C: keep index of first 0
    D: replace max_ones if necessary, and reset index to 1st zero

    0123456789012
    1110111101111
    i

    ones = 0, 4, 8 -> 1
    mo = 8
    i = 0 -> 8 -> 3 + 1 = 4
    zeros = 0, 1, 2
    first_z = 3

    1001011001

"""


class Solution:
    def flip_bit(self, num: int) -> int:
        """O(log(n)) time and space"""
        # validations/special cases:
        if isinstance(num, int) is False:
            raise ValueError("Please provide an integer value.")
        if num == 0:
            return 1
        # A: store bits in array
        bits = [int(bit) for bit in bin(num)[2:]]
        # B: count consecutive ones, (includes first zero) up to 2nd zero
        ones, max_ones = 0, 0
        zeros = 0
        index, first = 0, 0
        while index < len(bits):
            bit = bits[index]
            # if we have a 1, increase count of ones
            if bit == 1 or zeros < 2:
                ones += 1
            elif bit == 0:
                zeros += 1
                # C: keep index of first 0
                if zeros == 1:
                    first = index + 1
                # D: replace max_ones if necessary, and reset index to 1st zero
                elif zeros == 2:
                    if ones > max_ones:
                        max_ones = ones
                    zeros = 0
                    index = first
            # E: move on to the next iteration
            index += 1
        # F: return maximum length of 1's we can make
        return max_ones


"""
Code Trace:

num: 1775

        0123456789012
bits = [1110111101111]
           i

ones, max_ones , zeros,   first
0,       0,       0          0
1        8        1          3          
2                 2
3                 0
4
5
6
7
8
"""

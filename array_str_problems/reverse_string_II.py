class Solution:
    """
    Problem:

    Given a string and an integer k, 
    you need to reverse the first k characters for every 2k characters 
    counting from the start of the string. 
    
    If there are less than k characters left, reverse all of them. 
    If there are less than 2k but greater than or equal to k characters, 
    then reverse the first k characters and left the other as original.
    """
    def reverseStr(self, s: str, k: int) -> str:
        """
        Reverse At 2k intervals - len(s) > 2k
        Input: s = "abcdefg", k = 2
                    ^   ^
                    0123456
        reverse the first 2 char, for every 4 from the start
        
        Output: "bacdfeg"
        
        
        Reversing all the chars in the string
        len(s) < k
         abcdefg", k = 10
        
        Reverse Once:
        k <= len(s) < 2k
        abcdefg", k = 4 ---> gfedcba?
            ^    
        
        Insights:
        - need to do a reverse() at least 1
        
        Clarifying questions: 
        - input is mutable? yes
        - lower case English letters only 
        - no empty strings
        
        Intuition:
        - loop over the string (iterations)
        
        Approach:
        - reverse(int starting index, k) - helper function to do one reversal
        # init a count for num_reversals
        # iterate over the string
            # do a reversal 
                # check if it's goes beyond the edge
                # if it's the first, then do it anyway
                # if it's not the first, don't do it
                    # reverse()
            # move the index up 2k indices
                # do another reversal, if it won't cause us to go "off the edge"
            # increment the number of reversals
        # return the string
        0123456
        abcdefg, k = 2
        bacdfeg
        
        nr = 0, 1, 2
        str_index = 0, 4, 6, 8
        reverse[0:2]
        reverse[4:6]
        
        bacdefg
        ^      ^
        
        """
        # ---------- Helper ----------------------------------------
        def reverse(start, s):
            # A: calculate the ending index
            end = start + k - 1
            # 1     0     2.   1
            # prevent IndexErrors
            if end >= len(s):
                end = len(s) - 1
            # reverse the substring: we need only end - start - 1 swaps
            while start < end:  # both start and end should be w/in index bounds
                # B: swap the letters at start and end - 1 indices
                s[start], s[end] = s[end], s[start]
                # C: increment start, decrement end
                start += 1
                end -= 1
            return 
        # --------- Driver ----------------------------------------
        # init a count for num_reversals
        num_reversals = 0
        str_idx = 0
        s = list(s)
        # iterate over the string
        while str_idx < len(s):  # ceil(s / k) iterations - goes from 1 - s iterations
                                 #                                  lots  less time in rever
                                 #                                   of
                                 #                                 reverse()
            reverse(str_idx, s)  #                                         O(s)
            # move the index up 2k indices
            str_idx += (2 * k)
            # increment the number of reversals
            num_reversals += 1
        # return the string
        return ''.join(s)  # s iterations
    
"""
            0123456
Input: s = "bacdfeg", k = 2

nr      |      idx      |   start       |   end   
0               0            0                2
1               4            1                1
                             4                6
2               8            5                5
            
Input: s = "abcdef", k = 3
                  ^
nr      |      idx      |   start       |   end     |   s 
0               0             0               3        abcdef
                                                        0 1 2 3 4 5
                6             1               2        [c,a,b,d,e,f]
                                                       
Problem 2: reversal algorithm needs to work for all lengths

Time:  O(s)
Space: O(s) - since we require space for an array object of len(s)

s = 10,000
k = 1
    5,000 - O(s)
s = 1
k = 10,000 - O(1)

s = 10000
k = 10000 - O(1)

s = 2,500
k = 5

call reverse 500 times
each reverse = 10
            5000

"""
        
        
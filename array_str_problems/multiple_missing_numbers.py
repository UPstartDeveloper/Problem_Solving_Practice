"""
Given a list of distinct integers from 0 to a value MAX_VALUE, 
write a function to produce a string that describes the ranges of numbers missing from the list,
including MAX_VALUE.

The items in the result should be sorted in ascending order and separated by commas. 
When a gap spans only one number, the item is the number itself; 
when a gap is longer, 
the item comprises the start and the end of the gap, joined with a minus sign.


array is sorted
empty array is not possible - (note first entry could be other than 0)
MAX_VALUE will be given as input

I'll assume MAX_VALUE >= 0

Example:

MAX_VALUE = 1000
VALUES = [0, 1, 3, 50, 52, 75]
RESULT = "3-49,51,53-74,76-1000"
MISSING = [3,4,5,6,7,8,9,10]
           ^              ^
MY_RESULT = "3-current_value - 1", 

val = 50

if val is present
    # increment both idx and val
elif val is not present
    # start the next range, range = [val]
    # increment val
    # when val == values[idx]
        # if val - start > 2:
            # add val ot the range again (as the end)
        # join the range with a '-'
        # add the range to the output (as a string)



Brainstorm:

current_value = 3, 4, 5, 6, 7,... 49
        
        3
--------x------------------------------------------->
"""


class Solution:
    def multiple_missing_numbers(self, values, max_value):
        """Note: must add values as STRINGS"""
        val, idx = 0, 0
        output = list()
        while idx < len(values) and val < max_value + 1:
            # if val is present
            if val == values[idx]:
                # increment val and idx once
                val += 1
                idx += 1
            else:  # val is not present
                # start the next range, range = [val]
                range = list(str(val))
                # increment val until when val == values[idx]
                while val < values[idx]:
                    val += 1
                # if val - start > 2:
                if val - int(range[0]) > 2:
                    # add val it the range again (as the end)
                    range.append(str(val - 1))
                output.append(range)
        # add the last range, if max_value not in the array
        if val < max_value + 1:
            range = list([str(val)])
            if val < max_value:
                range.append(str(max_value))
            output.append(range)
        # add the ranges to the output (as a string)
        return ",".join(["-".join(range) for range in output])


if __name__ == "__main__":
    vals = [0, 1, 2, 50, 52, 75]
    max_value = 1000
    print(Solution().multiple_missing_numbers(vals, max_value))

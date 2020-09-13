"""
Solution for 
Sort Integers by The Power Value: https://leetcode.com/problems/sort-integers-by-the-power-value/
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Can I calculate the power of an integer?
        # if two ints have same power, sort by the ints
        # power of 1 = 0 steps
        # [1] -> 1
        # no zeros for now
        # assume no negatives
        def calculate_steps(range_int: int) -> int:  # i = range_int
            # init a variable to count the number of steps at 0
            steps = 0 
            # iterate while the number not equal to zero
            while range_int != 1:
                # transform it using the right eq, based on even or odd
                if range_int % 2 == 0:
                    range_int /= 2
                else: # should be odd
                    range_int = (3 * range_int + 1)
                steps += 1
            # return the steps
            return steps
        """
        steps = 9
        
        range_int = 1
        """
        power_ints = dict() 
        # n = hi - lo + 1
        # iterate over all the integers in the range
        for num in range(lo, hi + 1):  # n iterations
            # calulate the power of the integer
            power = calculate_steps(num)
            # map each integer of the power -> range_int
            if power in power_ints: # O(1)
                power_ints[power].append(num)
            else:
                power_ints[power] = [num]
        # sort the range ints into an seq, based on the powers
        sorted_powers = sorted(power_ints)  # O(n log n)
        sorted_ints = list()
        for power in sorted_powers:  # n iterations
            ints = power_ints[power]
            ints.sort()
            sorted_ints.extend(ints)  # 
        # return the k - 1 element
        return sorted_ints[k -1]
    
    # Time O(n * calculate_power + n log n)
    # Space O(n)
    
    """
    
    """
    """
    lo = 12
    hi = 15
    k = 2
    
    power_ints = {
        9: [12, 13]
        17: [14, 15]
    }
    sorted_powers = [9, 17]
    sorted_ints = [12, 13, 14, 15]
    ints = [14, 15]
    power = 17
    num = 12
    power = 9
    
    """
        
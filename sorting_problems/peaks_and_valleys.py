"""
Peaks and Valleys: 

In an array of integers, a "peak" is an element which is greater than or equal 
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. 

For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {S, 2} are valleys. 

Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

EXAMPLE
           p->
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}

Restate: the problem is essentially to rearrange the array to have one larger element, then one smaller?
         or vice versa?

Clarifying questions:

- I guess what I'm most concerned about is the distr of the integers
- so a peak can be comprised of more than just one integer, correct?
    - yes, because we don't consider numbers w/ respect to just their immediate neighbors
- each number can only be part of either a peak or valley? yes
- every number has to be either a p/v? yes

   p
{5, 3,    1, 2, 3}

Assumptions:
- duplicates in the array
- negatives can happen

Brainstorming:

input = {5, 1, 3, 2, 3}

intuition: swap numbers based on what we need next in the array
approach:
# A: first get the max element and put it in the first spot
# B: swap elements until we're in order
    # init the flag to look for <= elements
    # if the next element meets the condition,
        # move on the index to the next elem, 
    # otherwise if it doesn't meet the condition
        # swap this element and its next neighbor, move up the index
    # regardless, flip the flag for the next iteration

Edge Cases:

{7,7,7,7,,1, 77, 7,7,7,}

77, 7,7,7,77,7,7,,7,7,1,

"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def init_flag(self) -> int:
        """
        Look for the first value that's less/greater
        than the beginning of the array
        """
        # init to 1 (True value)
        should_be_less = 1
        # check to make sure the next element is not actuallly greater
        index = 1
        while index < len(self.nums):
            next_elem = self.nums[index]
            if next_elem > self.nums[index - 1]:
                should_be_less = 0
                break
            elif next_elem < self.nums[index - 1]:
                break
            else:  # next_elem == self.nums[index - 1]:
                index += 1
        return should_be_less

    def is_sorted(self):
        # A: init the bool flag
        should_be_less = self.init_flag()
        # B: check to make each subsequent element meets the flag condition
        index = 1
        while index < len(self.nums):
            next_elem = self.nums[index]
            prev_elem = self.nums[index - 1]
            # if not met, return False
            if should_be_less is False and next_elem <= prev_elem:
                return False
            if should_be_less is True and next_elem >= prev_elem:
                return False
            index += 1
        # C: if all is well, return True
        return True

    def sort_peaks_and_valleys(self):
        def swap(next, prev) -> None:
            self.nums[next], self.nums[prev] = self.nums[prev], self.nums[next]

        # A: sort elements until we're in order
        is_sorted = False
        while is_sorted is False:
            # B: init the flag to look for <= elements
            should_be_less = self.init_flag()
            # prep for swapping
            index = 1
            swaps = 0
            while index < len(self.nums):
                next_elem, prev_elem = self.nums[index], self.nums[index - 1]
                # otherwise if it doesn't meet the condition
                if should_be_less == 0 and next_elem < prev_elem:
                    # swap this element and its next neighbor,
                    swap(index, index - 1)
                    swaps += 1
                elif should_be_less == 1 and next_elem > prev_elem:
                    # swap this element and its next neighbor,
                    swap(index, index - 1)
                    swaps += 1
                # regardless, flip the flag for the next iteration
                index += 1
                should_be_less = 0 if 1 == should_be_less else 1
                print(self.nums, index, should_be_less)
            # judge if we're sorted
            is_sorted = swaps == 0
        return None


if __name__ == "__main__":
    nums = [[5, 3, 1, 2, 3], [7, 7, 7, 7, 77, 17, 7, 7]]
    for arr in nums:
        sol = Solution(arr)
        print(f"Nums before: {sol.nums}")
        sol.sort_peaks_and_valleys()
        print(f"Nums after: {sol.nums}")


"""
 0  1  2  3  4
[5, 1, 3, 2, 3]
          p  n
SBL     IS      i   s
T       F       1   0
F       F       2   1
T               3   0
F               4
                5
                1

"""

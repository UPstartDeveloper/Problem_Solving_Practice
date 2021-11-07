from typing import List


def find_unsorted_subarray(nums: List[int]) -> List[int]:
    # Init start pointer to -1
    start = 0
    # iterate over the list
    while start < len(nums):
        # iterate from the end towards the start
        end = len(nums) - 1
        while end > start:
            # check that the subarray is sorted
            start_num, end_num = nums[start], nums[end]
            if end_num < start_num:  # solution found
                # avoid IndexError as we return solution
                if end < len(nums) - 1:
                    return [start, end + 1]
                else:
                    return [start, end]
            # otherwise keep moving the end back
            end -= 1
        # Move the start pointer towards the end of the array
        start += 1
    # If I get outside the for loop, then [-1, -1]
    return [-1, -1]


if __name__ == "__main__":
    nums = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(find_unsorted_subarray(nums))

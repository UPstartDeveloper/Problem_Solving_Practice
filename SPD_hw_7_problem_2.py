'''
Problem description and starter code found on LeetCode:
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
'''
Variable Table:
Variable     |    nums1    |   nums2   |  merged   |
Values       |   [1, 3]    |     [2]   |     []    |
                                       |           |  index1  |   index2  |
                                       |           |   0      |    0      |  num1  |  num2   |
                                       |           |          |           |  1     |   3     |
                   [3]     |           |     [1]   |          |           |
                           |     []    |   [1, 2]  |
                           |           | [1, 2, 3] | mid_index|  middle   |
                                                   |    2     |   2
'''


def find_median_sorted_arrays(nums1, nums2) -> float:
    '''Merges two sorted lists of numbers, and returns the median of all.'''
    # create a new list of all items in order
    merged = list()
    index1, index2 = 0, 0
    while index1 < len(nums1) and index2 < len(nums2):
        num1, num2 = nums1[index1], nums2[index2]
        # decide which number takes the next spot in merged
        if num1 <= num2:
            merged.append(nums1.pop(index1))
        else:  # num1 < num2
            merged.append(nums2.pop(index2))
    # if lists of unequal size, then we add all remaining from the non-empty
    if len(nums1) > 0:
        merged.extend(nums1)
    else:  # len(nums1) == 0, and len(num2) > 0
        merged.extend(nums2)
    # determine middle index and element of the array
    mid_index = len(merged) // 2
    middle = merged[mid_index]
    # if the list has odd number of elements, we know what to return!
    if len(merged) % 2 > 0:
        return middle
    else:  # len(merged) == 0
        # return the mean of the two elements in the middle
        return (middle + merged[mid_index - 1]) / 2


if __name__ == '__main__':
    # test on good inputs
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2

    nums1 = [1, 2]
    nums2 = [3, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

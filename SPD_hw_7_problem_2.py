'''
Problem description and starter code found on LeetCode:
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
'''
Variable Table:
Variable     |
Values       |

'''


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    '''Merges two sorted lists of numbers, and returns the median of all.'''
    pass


if __name__ == '__main__':
    # test on good inputs
    nums1 = [1, 2]
    num2 = [3, 4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.5

    nums1 = [1, 3]
    num2 = [3]
    assert find_median_sorted_arrays(nums1, nums2) == 2

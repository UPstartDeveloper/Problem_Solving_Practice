from typing import List


class Solution:
    def find_median_old(self, nums1: List[int], nums2: List[int]) -> int:
        # merge the sorted lists
        sorted_array = list()
        # store the lengths of both input lists
        nums1_amt, nums2_amt = len(nums1), len(nums2)
        nums1_index, nums2_index = 0, 0
        # merge the two lists
        while nums1_index < nums1_amt and nums2_index < nums2_amt:
            # get the smallest elements in each list
            num1, num2 = nums1[nums1_index], nums2[nums2_index]
            # decide which should go in the merged list next
            if num1 <= num2:
                # add the number
                sorted_array.append(num1)
                nums1_index += 1
            else:  # num2 < num1
                sorted_array.append(num2)
                nums2_index += 1
        # add any remaining elements
        if nums1_index < nums1_amt:
            sorted_array.extend(nums1[nums1_index:])
        elif nums2_index < nums2_amt:
            sorted_array.extend(nums2[nums2_index:])
        # find the value at or near the middle of the array
        index = (nums1_amt + nums2_amt) // 2
        median = float(sorted_array[index])
        # compute the median for an even number of elements
        if (nums1_amt + nums2_amt) % 2 == 0:
            # get the other addend for the mean
            other_middle = float(sorted_array[index - 1])
            median = (median + other_middle) / 2.0
        return median

    def find_median_new(self, arr1: List[int], arr2: List[int]) -> int:
        # TODO: handle the case where the arrays are distinct
        if arr1 is None or len(arr1) == 0:
            raise ValueError("There is nothing in array 1")
        if arr2 is None or len(arr2) == 0:
            raise ValueError("There is nothing in array 2")
        # init the range over which we are searching
        low1, high1 = 0, len(arr1) - 1
        low2, high2 = 0, len(arr2) - 1
        # compare the medians of both arrays
        median = None
        while True:
            mid1, mid2 = ((low1 + high1) // 2, (low2 + high2) // 2)
            med1, med2 = arr1[mid1], arr2[mid2]
            # medians match -> return the answer
            if med1 == med2:
                median = med1
                break
            # median1 > median2
            elif med1 < med2:
                high1 = mid1
                low2 = mid2
            # median1 < median2
            else:
                low1 = mid1
                high2 = mid2

        # there's an error if median is None
        return median

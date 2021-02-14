from typing import List

class Solution:
    def find_median(self, arr1: List[int], arr2: List[int]) -> int:
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
            mid1, mid2 = (
                (low1 + high1) // 2, (low2 + high2) // 2
            )
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
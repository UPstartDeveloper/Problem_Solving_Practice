class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        Idea 1: brute force
        1. extend one array by the other
        2. sort again
        3. return the value at the middle index (calculate the middle)
        
        O(n log n)
        
        Idea 2: combine the two sorted lists by merging
        
        1) merge the lists in sorted order
        2) return the median of the dataset
        
        O(n + m) time
        O(n + m) space
        
        Idea 3: averge the medians of each list individually
        
        but this wouldn't work, if all the values in one list are larger/smaller 
        than those of the other
        
        [1,2, 3], [10]
        
        nums1 = [1, 2]
        nums2 = [3, 4]
        
        sorted_array = [1, 2, 3, 4]
        
        nums1_amt = 2
        nums2_amt = 2
        
        nums1_index = 2
        nums2_index = 
        
        index = 2
        median = 3
        
        should this algorithm be stable? If so do nums1 get to go first?
        """
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

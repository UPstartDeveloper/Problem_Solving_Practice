from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Leetcode: https://leetcode.com/problems/merge-sorted-array/
        Do not return anything, modify nums1 in-place instead.
        
        Input:
            2 sorted int []'s 
            nums1 mutable
            can be empty
            can haves dupes
            
            index of last "real" elem in nums1: len(nums1) - len(nums2)
            total_len = len(nums1) = tl = n+m
            
            len(nums1) > len(nums2)
            
            
            Approach:
            
                A: merge nums2 into nums1:
                    iterate over the first (tl - m) spaces
                        if n1 <= n2 --> just move on
                        if n1 > n2 --> swap n1 and n2
                B: merge rest of nums2
                    copy vals from nums2 into the end of nums2
        """
        index1, index2 = 0, 0
        merged = []
        # A: merge nums2 into nums1:
        while index1 < m and index2 < n:
            if nums1[index1] <= nums2[index2]:
                merged.append(nums1[index1])
                index1 += 1
            else:
                merged.append(nums2[index2])
                index2 += 1
        # merged the rest
        if index1 < m:
            merged.extend(nums1[index1:])
        elif index2 < n:
            merged.extend(nums2[index2:])
        # C: overwrite nums1
        for index1 in range(len(nums1)):
            nums1[index1] = merged[index1]

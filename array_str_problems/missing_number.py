class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/missing-number/
        
        Input:
            arr of n non-neg values
            unsorted
            immutable
            unique
            
        Output:
            int in the range(0, n) that's not in the arr
                        (n + 1 values)
        
        Intuition
            hashset
            sorting
            
        EC:
            empty arr --> 0
            non-int, neg --> ValueError
            1 elem --> O or 1, depending on what's in arr
        
        Approach:
        
            1) Brute Force --> O(n^2)
                linear search for each value in range
                
            2) Sort the array --> O(n log n)
                1 pass --> return the value != index, or len
                
            3) Hashset --> O(n) time, O(n) space
                create a set of {0...n}
                create a set from arr
                return set - arr_set
                
            4) Using addition + subtraction
                calculate sum(range(0, n))
                subtract sum(arr)
                return diff
                        
        """
        return sum(range(len(nums) + 1)) - sum(nums)
        

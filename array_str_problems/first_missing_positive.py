class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/first-missing-positive/
        
        Input:
            int[signed 32-bit, dupes, unsorted].len > 0
            could be any range basically 
            immutable
            
        Output:
            min(missing > 0)
            missing = int not in the array
            
        Intuition:
            search/sorting?
            hashset?
            heap?
            
        EC:
            [] --> 1, or ValueError
            all neg or 0 --> 1
            all pos --> return n
            int out of range --> ValueError
            
        Stepping Stone Problems:
        1) find smallest int in arr
            --> linear search
            
        2) find smallest pos int in array
            --> linear search + condition > 0
            --> if no pos --> return 0
            
        3) find smallest pos int not in array
            do 2) -- min pos int in array
                if 0 or >1 --> return 1
            else if 1 --> ???
                how many other pos ints in the array?
                also find the max pos int in array
                answer is either max+1, OR "in-between"
            
        Approach:
            
            1) Brute force Search: --> O(n^2), sorted arr>0
                linear search for 1 in array,
                then linear search for 2,3,4...
                
                iterate on min ints>0 --> until missing found
                
            2) Sorting --> O(n log n) + O(log n)
                sort the array 
                binary search for 0 --> find closest
                
            3) Hash Set: 
                s1 create a set of values {1 ... n + 1}
                s2 create a set of all pos in arr
                s1 =- s2
                return min(s1)
            
            
            TODO - O(n) time, O(1) space
        
        """
        all_pos = [num for num in nums if num > 0]
        present_pos = set(all_pos)
        smallest_pos = set(range(1, len(all_pos) + 2))
        missing_pos = smallest_pos - present_pos
        return min(missing_pos)

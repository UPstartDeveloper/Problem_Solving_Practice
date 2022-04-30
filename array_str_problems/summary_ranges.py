from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        LeetCode: https://leetcode.com/problems/summary-ranges/
        
        Input:
            int[small, immutable, sorted, distinct, pos/neg]
            
        Out:
            list[ranges]
                range - inclsuive
                corr to a subarray
                ASSUME nnneds to be sorted
                
        Intuition:
            Pointers - O(n) O(1)
            Set - O(n), O(n)
            
        EC:
            empty array - []
            dupes - ValueError
            
        Approach:
            1) Pointers
                init output = [], index = 1
                start_of_first_rannge = 1st elemm
                traverse the array
                    current_last = start_range
                    while elem == current_last + 1
                        update current_last
                        move fwd
                    on break:
                        add the next range using start_range, current_last
                        update start_range = elem
                        
                return output
                    
        
        """
        # Edge Case
        if len(nums) == 0:
            return []

        # Find the value where each range "begins"
        starts = [nums[0]]
        starts.extend(
            [
                elem
                for index, elem in enumerate(nums)
                if index > 0 and elem >= nums[index - 1] + 2
            ]
        )

        # Locate the correspond end value for each range
        ends = [
            elem
            for index, elem in enumerate(nums)
            if index < len(nums) - 1 and elem <= nums[index + 1] - 2
        ]
        ends.append(nums[-1])

        # Form the output
        out = []
        for start, end in zip(starts, ends):
            # add a single range to the output
            if start == end:
                out.append(str(start))
            else:
                out.append(f"{start}->{end}")

        # All done!
        return out

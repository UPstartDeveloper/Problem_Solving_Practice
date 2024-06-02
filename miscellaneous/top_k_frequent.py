class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Link: https://neetcode.io/problems/top-k-elements-in-list
        
        nums - dist of int
            -1000 ---> 1000 inclusive
            not always sorted 
            no []'s

        k 
            1 ---> len(set(nums))

        Intuition
            counting sort-based approach

        EC
            TODO

        Approach

        example:
            nums = [1,2,2,3,3,3]
            freq_dist = [1, 2, 3]
            --- how to get to the following?? ---- 
            top_k = [
                [3, 3]
                [2, 2]
                [1, 1]
            ]

            out = [2, 3] OR [3, 2]

        1. Counting Sort ---> O(n log n) time, O(1) space 

            int's 
            in a known range

            - init an array for the dist --> int[2001] 0's 
            - populate the array - using nums ---> 2D freq dist of the nums - O(1) 
            - sort the freq dist by FREQ ---> O(2001 log (2001)
            - return top k VALUES 

        2. Hashmap as the Freq Dist
            - not as fast to get top K freq

        3. Min Heap - O(n log k) time + O(k) space

            - init an array for the dist --> int[2001] 0's 
            - populate the array - using nums ---> 2D freq dist of the nums 
            - sort by top k greatest frequency --> O(n log k)
            
        """

        # - init an array for the dist --> int[2001] 0's 
        freq_dist = [
            # val, count
            (0, 0) for (_, _) in range(-1000, 1001)
        ]

        # - populate the array - using nums ---> 2D freq dist of the nums - O(1) 
        for index, val in enumerate(nums):
            fd_index = val + 1000
            _, current_freq = freq_dist[fd_index]
            freq_dist[fd_index][1] += 1  # update count 

        # - sort the freq dist by FREQ ---> O(2001 log (2001)
        freq_dist.sort(key = lambda val, count: count, reverse=True)

        # - return top k VALUES 
        return [
            val for [val, _] in freq_dist[:k]
        ]


        

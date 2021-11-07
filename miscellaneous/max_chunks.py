class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        given an array of integers
        duplicates can occur
        returbn an integer

        want the max number of chunks need

        can we have nested chunks

        Goal:
        trying to sort the list
        divide and conquer, similar but not quite the same to one's such as merge

        Divide step:
        - divying up the list into chunks, which when sorted form a sorted verstion of the original
        - conquer by then merging the sublists back together

        - UNLIKE mergesort though, we have to keep where the positions of the sublists the same
                - the positions of the elements in each sub list can change
                - but not the position of the sublists to each other
        - Goal:
        - how many chunks we need to make in the divide step - localizes the problem

        Insights:
        - (comparision to merge sort): we eventually have n sublists of size 1, for each of n elements
        - in this problem though, there are inputs as example 1, where when the input is in complete reverse
            order, it's gotta be 1 sublist -
            [5] [4]  [3]  [2]  [1]

        Idea 1: using comparisions
        A: init a counter for the number of chunks at 1 -> answer's >= 1
        B: iterate over the list, starting from index 0 to second to last index
            a) whenever the (! prev > next), increment chunks by 1
            b) incremet the index
        C: return the number of chunks

        arr                 chunks             index            prev            next
        [5,4,3,2,1]             1                  0            5                 4
                                                   1            4                 3
                                                   2            3                 2
                                                   3            2                 1

        arr                 chunks             index            prev            next
        [2,1,3,4,4]             1                  0            2        >         1
                                2                  1            1        <         3
                                3                  2            3.       <.        4
                                4                  3            4        =         4

        Time: O(n)
        Space: O(1)

        Example three:
        [6, 7, 7, 1, 5, 8]
        [6, 7, 7, 1, 5], [8] --> 2

        [6, [7], [7], 1, 5], [8] --> 4

        """
        # A: init a counter for the number of chunks at 1 -> answer's >= 1
        chunks = 1
        # B: iterate over the list, starting from index 0 to second to last index
        index = 0
        NUMS = len(arr)
        while index < NUMS - 1:
            # a) whenever the (! prev > next), increment chunks by 1
            prev, next_int = arr[index], arr[index + 1]
            if prev <= next_int:
                chunks += 1
            #  b) incremet the index
            index += 1
        # return the answer
        return chunks

        """
        Example three:
        [6, 7, 7, 1, 5, 8]
        
        chunks = 1      | 1
        index  = 0      | 
        NUMS   = 6      |
        prev   = 6      |
        next_int = 7    |
        
        """
        """
        Example three:
         0  1  2  3  4
        [4, 2, 2, 1, 1]
        NUMS   = 5
        iterate from indices 0 to 3
        
        
        chunks = 1      | 1
        index  = 0      | 
        NUMS   = 6      |
        prev   = 6      |
        next_int = 7    |
        
        Idea #2: - two point
        
        early to the problem:
        - find the index of the largest number,
            and if it's at 0 --> return 1
            
        - whatever the sublist is, it's gotta have a max, and include all the int's < max, and has a
            greater index in the original array
            
            [4,2,2,1,1]
             ^       ^
             
             chunks = 1
             DOES NOT increment
             
             [6, 7, 7, 1, 5, 8]
                             ^           ^
              
              chunks = 1
             DOES NOT increment
             chunks 2
        """

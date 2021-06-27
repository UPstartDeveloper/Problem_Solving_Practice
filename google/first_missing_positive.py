class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        unsorted array
        pos and neg
        answer must be POSITIVE Int
        
        start in the range 1.... positive inf?
        
        32-bit ints
        
        ASSUME 
        size of array fits in memory
        
        Hints:
        - Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
        - We don't care about duplicates or non-positive integers
        - Remember that O(2n) = O(n)

        Intution:
        linear search for smallest missing pos int
        
        Approach:
        
        1. DIY: --> n * p (p = # of positive nums already presrnt)
            checking which positive nums I have in the array --> helps us find the smallest missing
            A: find the range of nums ---> min, max
            B: if min > 1 --> return 1
            C: iterate over all the positive nums (1, 2, 3...)
                D: nested, check for that positve
                
        2. Set --> Linear in Time, Linear Spacw
            A: find the min and max
            B: if min > 1 --> return 1
            C: find the first smalllest pos int
            1 ---> check if it's in the set
                - if so --> move on
                - otherwise, return the num
            D: if reache outside the pos max

            [ 0    1.    2   ]

            <0 ----1------2-----3 -->
        
        3. Sort the Array --> n log n
            A: sort the array
            B: traverse the array
            C: return the first val != index + 1
         0  1. 2.  3
        [0, 1, 2]
        
        
        4. Size
        - range of values -- [low, high]
        B: if min > 1 --> return 1
        C: max
        Edge Cases:
        no empty array
        duplicates - not bad (always)
        smallest positivie is outide ---> outside the array
        
        
        """
        """
        # A: find the min and max
        mi, ma = min(nums), max(nums)
        # B: if min > 1 --> return 1
        if mi > 1:
            return 1
        # C: find the first smalllest pos int
        num_set = set(nums)
        # 1 ---> check if it's in the set
        current_pos = 1
        while current_pos in num_set:
            # if so --> move on
            current_pos += 1
        # D: missing num found
        return current_pos
        """
        # A: check for 1
        if min(nums) > 1:
            return 1
        # B: init subrange
        sub = [1, max(nums)]
        # C: find the missing num, and return it
        for val in nums:
            if val > 0:
                # "move up" the val we think is missing
                if val == sub[0]:
                    sub[0] += 1
                # move down the top of the subrange of missing
                elif val < sub[1]:
                    sub[1] = val
        # bottom of the subrange is already present
        if sub[0] == sub[1] or sub[0] == max(nums):
            return max(nums) + 1
        # otherwise, the answer may be the bottom of the sub range
        return sub[0]
    
        
        
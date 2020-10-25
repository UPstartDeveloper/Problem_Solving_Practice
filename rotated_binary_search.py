class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot > 0
        """
        brute force = linear search
        All values of nums are unique.
        
        # pivot > 0
        
        Idea #1
        - undo the pivot - n
        
        [4,5,6,7,0,1,2] -> [0, 1, 2, ,3 4, 5, 6, 7]
        - binary search - log(n)
        
        Idea #2 - modified binary search (offset)
        
        [4,5,6,7,0,1,2], target = 0
        7 > 0
        we would go left, right instead
        
        reverse the directions 
        less than --> right half
        greater than --> left 
        
        [0,1,2,3,4,5,67]
        
        [6,5,4,7,3,9,2]  -> pivot = 4 right rotations
         l           h
         m
         --------------
         [4,5,6,7,0,1,2]
                l     h
                  m
        low = 0
        high = 6
        
        mid = 3, firs 
        + pivot
        = 7 % len(array) - 1 = 0
        
        compare mid with target
        0 < 4
        
        low = 0
        high = 
        
        
        How to Find the Pivot:
        - pivot = index of min 
        
        
        [3, 4, 5, 6, 1, 2]
        
        go to the middle
        
        compare middle with target
        
        if target == middle 
            return index of middle
        otherwise if not equal, and it's the last possible index
            return -1 (negative answer)
            
        otherwise keep 2 additional pointer (one to the left and right of middle)
        see which of those values is closer to the target
        go search that half of the array
            
        """
        def rotated_binary_search(low, high):
            # go to the middle
            middle_index = ((low + high) // 2)
            # compare middle with target
            mid = nums[middle_index]
            # see if found the target
            if target == mid:
                return middle_index
            # otherwise if not equal, and it's the last possible index
            elif low >= high:
                return -1 
            # otherwise
            else:
                # keep 2 additional pointers (one to the left and right of middle)
                if 0 < middle_index < (len(nums) - 1):
                    # see which of those values is closer to the target
                    left_side = nums[middle_index - 1]
                    # left_side = nums[0]
                    right_side = nums[middle_index + 1]
                    # right_side = nums[len(nums) - 1]
                    # go search that half of the array
                    left_dist_sq = (target - left_side) * (target - left_side)
                    right_dist_sq = (target - right_side) * (target - right_side)
                    print(f'Left Dist: {left_dist_sq}, Right Dist: {right_dist_sq}')
                    print(f'Middle: {mid}, low: {low}, and high: {high}')
                    if left_dist_sq < right_dist_sq:
                        # go search the left side
                        return rotated_binary_search(low, middle_index - 1)
                    else:
                        # search the right side
                        return rotated_binary_search(middle_index + 1, high)
                # just search the right side by deafult
                """elif middle_index == 0 and middle_index < len(nums):
                    return rotated_binary_search(middle_index + 1, high)
                # just search the left by default
                elif middle_index == len(nums) - 1 and middle_index > 0:
                    return rotated_binary_search(low, middle_index - 1)"""
                print('not in any if statements!')
                print(f'Middle: {mid}, low: {low}, and high: {high}')
                return -1
        # --------------------------------------------------------------------
        return rotated_binary_search(0, len(nums) - 1)               
"""
nums = [4,5,6,7,0,1,2], target = 0

SF 1
low = 0
high = 6
middle_index = 3
mid = 7

LS = 6
RS = 0
LSD = 36
RSD = 9


SF 2
low = 4
high = 6
middle_index = 5
mid = 1

SF 3
low = 4
high = 4
middle_index = 4
mid = 0

"""
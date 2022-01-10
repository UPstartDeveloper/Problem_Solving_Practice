from typing import List


class Solution:
    ### HELPER
    def binary_search(self, nums: List[int], target, low_index: int, high_index: int):
        # calculate the middle index
        mid_index = (low_index + high_index) // 2
        # get the element at the middle
        middle = nums[mid_index]
        # target found
        if middle == target:
            return mid_index
        # if middle is less
        elif middle < target:
            # if it's the last possible element
            if low_index == high_index:
                # then the element should be at that index
                return mid_index + 1
            # otherwise search the upper half
            return self.binary_search(nums, target, mid_index + 1, high_index)
        # if middle is greater
        elif middle > target:
            # if it's the last possible element
            if low_index == high_index or low_index == mid_index:
                # target expect one past the middle
                return mid_index
            # otherwise search the lower half
            return self.binary_search(nums, target, low_index, mid_index - 1)

    ### DRIVER
    def searchInsert(self, nums: List[int], target: int) -> int:
        # execute a modified binary search on the list
        return self.binary_search(nums, target, 0, len(nums) - 1)


"""
Leetcode: https://leetcode.com/problems/search-insert-position/

mid = 1
[1,3,5,6]

[1], low == high --> return one greater than middle
______________

[1,3,5,6]

[5, 6]
[6] , low == high --> return one greater than middle

_______________________
nums = [1,3,5,6]

target = 7

  3.      3.           3.           3.         6
  2.      2.           3            2.         5       
  1.      0.           3.           1          3      
call | low_index | high_index | mid_index | middle 
_______________________
nums = [1,3,5,6]

target = 0 -- return 0

  
  2.      0.            0.          0.        1
  1.      0.            3.          1.        3     
call | low_index | high_index | mid_index | middle 

_______________________
nums = [1,3]

target = 0

  2.     0.           -1
  1.     0             1.           0.         1   
call | low_index | high_index | mid_index | middle 



"""

"""
Problem:

A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.
"""


def shifted_arr_search(shiftArr, num):
    """
  Input:
    shiftArr:
      non-empty
      kinda sorted --> "rotated"
      unique
      pos/neg
    
    num: assumed in arr
    
  Output: index, or -1
  
  Intuition:
    search
   
  EC:
    - num not in arr --> -1
    - empty arr[] --> raise ValueError
    
  Approach:
  
    1) linear search - O(n) time, O(1) space
    2) optimal approach:
      
              t
  [9, 12, 17, 2, 4, 5]
   l       m        h
              l  m  h
              m
              
      2 < 17  
      
   9 < 2 < 17
   
  Stepping Stone:
  
    1) find the two ranges
      - linear pass - O(n)
    
    2) 2 x binary search - O(log n)
    
    
    binary search - modified:
    
      low, high = 0, last_index
      
      while loop
        
        mid value --> (low + hi) // 2
        check which range it's in
        
          if mid > high
            "left"
           
          else: --> "right"


        Base case
          target == mid:
            return the current index

        Recursive Cases:
        1) if target < mid:
                                      v      v   v
           if mid in "left"
             recurse on the right

           elif mid in "right"
          
          
          
  """
    # iterative, binary search

    low, high = 0, len(shiftArr) - 1
    target = num

    while low <= high:

        mid_index = (low + high) // 2

        mid_value = shiftArr[mid_index]

        # base:
        if target == mid_value:
            return mid_index

        # go left - TODO
        elif shiftArr[low] <= target < mid_value:
            high = mid_index - 1

        # go right - TODO[test]
        elif shiftArr[high] < mid_value and target <= shiftArr[high]:
            low = mid_index + 1

        elif mid_value < target <= shiftArr[high]:
            low = mid_index + 1

        else:
            break

    return -1

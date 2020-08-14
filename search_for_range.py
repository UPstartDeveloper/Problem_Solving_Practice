"""
Range -> because all the integers are sorted, we can return the first
         and last index of where that value appears (and it will be consecutive)
         (can they be the same value?)
         
O(log n), sorted list -> leads me to think this is some sort of application of 
          BS 
          
Idea #1 
A: First Search
- BS for the first/possibly only appearance
  - range list starts at [-1, -1], first index modified if target found 
    - if the search returns -1, return the range returns unmodified
    - if the search changes the range so first != second, then move on
    - if the search makes both indices the same, then return modified range (only 1 appearance)
B: Second Search:
  - check middle of range
  - if middle == target and is not the end/first
    - check if the next element also equals target
      - if it does, recurse over the range(next to middle, end)
    - otherwise update the end of the range to return
    
Idea #2 

A: Search for the First Appearance
  - just like normal BS, except:
    - if the middle value == target and mid_index != end:
      see if the previous element also == target:
        - if it does, then recurse over the range to left
          (just like if middle was less)
  - place the value returned by this in the first index of the range
    
B: Search for the Last Appearance 
  - just like A, except now we will search over the larger half if:
    - middle > target OR value at mid_index + 1 == target
  - place the value returned by this in the second index of the range
    
# is it okay to return a tuple, or does the output value need to be a dynamic 
array? It seems like from the problem description we need to use [], and I guess my brain associates
that with the list data type in Python, but we don't necessarily need that for this problem
  
"""

def search_for_range(array, target):
  def calculate_middle(lo, hi):
    # calculate middle index and value
    print(f'Lo: {lo} and hi: {hi}')
    mid_index = int((lo + hi) / 2)
    mid_value = array[mid_index]
    return mid_index, mid_value
  def search_for_first(low_index, high_index):
    '''Find the start of the range'''
    # find the middle
    mid_index, mid_value = calculate_middle(low_index, high_index)
    # if we think the value may appear in the lower half
    if mid_value > target or (mid_index >= 1 and array[mid_index - 1] == target):
      return search_for_first(low_index, mid_index - 1)
    # or if the value may appear on the right half
    elif mid_value < target:
      return search_for_first(mid_index + 1, high_index)
    # or we might just find the value
    elif mid_value == target:
      return mid_index
    # or it may not exist
    elif low_index == high_index:
      return -1
  def search_for_last(low_index, high_index):
    '''Find the end of the range'''
    # find the middle
    mid_index, mid_value = calculate_middle(low_index, high_index)
    # if we think the value may appear in the right half
    if mid_value < target or (mid_index < LAST_INDEX and array[mid_index + 1] == target):
      return search_for_last(mid_index + 1, high_index)
    # or if the value may appear on the left half
    elif mid_value > target:
      return search_for_last(low_index, mid_index - 1)
    # or we might just find the value
    elif mid_value == target:
      return mid_index
    # or it may not exist
    elif low_index == high_index:
      return -1
  # find the start of the range
  LAST_INDEX = len(array) - 1
  range_start = search_for_first(0, LAST_INDEX)
  # early exit: if we can't find a first appearance, then we can stop
  if range_start == -1:
    return [-1, -1]
  # otherwise, find the end of the range
  range_end = search_for_last(range_start, LAST_INDEX)
  return [range_start, range_end]
  
  
"""
Variable Value Trace:

          0  1  2  3  4   5
array =  [5, 7, 7, 8, 8, 10]

target = 8

LAST_INDEX = 5

low_index |  high_index  |    mid_index   |     mid_value   |     
    0           5                 2                 7
    3           5                 4                 8
    3           3                 3                 8
    
range_start = 3

low_index |  high_index  |    mid_index   |     mid_value   |
    3           5                 4                 8
    
range_end = 4
"""

print(search_for_range([5, 7, 7, 8, 8, 10], 8))

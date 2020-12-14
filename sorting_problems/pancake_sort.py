"""
# reverses the first k elements of an array
def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]

def pancake_sort(nums):
    '''
    Insight:
    - placing elements in proper position in reverse
    - move the element that belongs in the back, to index 0
    - then, flip for however many k is needed to move it to the correct spot
    
    A: start end_index = end of array
    B: for each subset of the array
        - find the largest value - aka, the one that belongs at back
        - <do something to move it to index 0> - use index + 1 flips
        - then flip by the index, to get it in the right spot
        - once in the right position, decrement the end index
    '''
    # A: start end_index = end of array
    end_index = len(nums)
    # B: for each subset of the array, iterate to move the max to the right spot
    while end_index > 0:
        # find the largest value - aka, the one that belongs at back of subset
        sub_max = max(nums[:end_index])
        print(f'Nums before: {nums}')
        print(f'Max is {sub_max}')
        # find the current index of the max 
        sub_max_index = nums.index(sub_max)
        # get the max at the front
        if sub_max_index > 0:
            flip(nums, sub_max_index + 1)
        # get the max into its sorted positon
        flip(nums, end_index)
        # move on to the next subset
        end_index -= 1
        print(f'Nums after: {nums}')
    return nums
"""   
def pancake_sort(arr):
  def find_max(num_elem_to_find_max):
    # find the idx of bigggest among num elems
    # linear search
    max_num = float('-inf')
    max_index = -1
    index = 0
    while index < num_elem_to_find_max:
      num = arr[index]
      if num > max_num:
        max_num = num
        max_index = index
      index += 1
    return max_index
  def flip(arr, k):
    # slice the array
    slice_arr = arr[:k]  # n 
    # reverse the slice
    slice_arr.reverse()  # n
    # put it in back the array
    for index, num in enumerate(slice_arr):  # n
      arr[index] = num
    return None
  num_elem_to_find_max = len(arr)  # constant 
  while num_elem_to_find_max > 1:  # n iterations
    # linear search to find max in that num
    max_index = find_max(num_elem_to_find_max)  # n
    # flip it by that index + 1
    flip(arr, max_index + 1)  # n
    flip(arr,  num_elem_to_find_max)
    # decrement the num of elements left to sort
    num_elem_to_find_max -= 1
  return arr
    


if __name__ == '__main__':
    # nums = [5, 2, 3, 4, 1]
    # nums = [2, 2,2,2,2,2,22,2,2,2,2, 6, 3,3, 1,2,2,2,2,22,2,2]
    nums = [38, 27, 43, 3, 9, 82, 10]
    print(pancake_sort(nums))
    
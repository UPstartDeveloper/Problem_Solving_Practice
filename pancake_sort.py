# reverses the first k elements of an array
def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]

def pancake_sort(nums):
    """
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
    """
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
    

if __name__ == '__main__':
    nums = [5, 2, 3, 4, 1]
    print(pancake_sort(nums))
    
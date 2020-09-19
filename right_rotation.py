from typing import List


def rotate_array(input_array, k):
    '''Perform k right rotations on input_array, in O(1) memory.'''
    for _ in range(k):
        # index the element from right
        last = input_array[-1]
        # copy element from front into a temporary variable
        first = input_array[0]
        # move the last element into the first index
        input_array[0] = last
        # shift all other elements to the right
        for index in range(1, len(input_array)):
            # use another temp variable for the value currently in array
            temp = input_array[index]
            input_array[index] = first
            first = temp


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """
        0 1 2 3 4 5 6 
    [1,2,3,4,5,6,7], k = 3
    
    5,6,7 + 1,2,3,4
    
    Idea #1 - list with swaps
    A: calculate the number of rotations that really need to occur
        - O(n)
    B: grab the elements that moving left
        - depends on the implementation
            - for loop and continue with the list
            - are we able to mutate the nums List into another data type, 
                like a deque?
    C: swap the elements at the first k indicies, with those in the last k - O(k % n) iterations
    [1,2,3,4,5,6,7]
    5, 2, 3, 4, 1, 6, 7
    5, 6, 3, 4, 1, 2, 7
    5, 6, 7, 4, 1, 2, 3
    D: move the elements in between the first and last k elements, and 
        move them to the back
    5, 6, 7, 4, 1, 2, 3 -> 5, 6, 7, 1, 2, 3, 4
        (k % n) * (n - 2(k % n))
        pop         iterations
        
    Space = O(1)
    Time: O((k % n)  +  (k % n) * n - 2(k % n))
        
    Is the time better than O(n)?
    """
    # A: calculate the number of rotations that really need to occur
    NUM_ELEM = len(nums)
    required_rotations = NUM_ELEM - (k % NUM_ELEM)
    # 82 % 53 -> 29
    # 53 - 29 = 14
    # B: swap the elements at the first k indicies, with those in the last k
    index_left, index_right = 0, NUM_ELEM - required_rotations
    for _ in range(required_rotations):
        elem_left, elem_right = nums[index_left], nums[index_right]
        nums[index_left], nums[index_right] = elem_right, elem_left
        index_left += 1
        index_right += 1
        print(f'Nums after {_ + 1} iterations: {nums}')
    # C: move the elements in between the first and last k elements, to the end
    print(index_left, index_right)
    for _ in range(index_left, index_right - required_rotations):
        nums.append(nums.pop(index_left))
        

if __name__ == "__main__":
    arr = list(range(1, 54))
    k = 82
    rotate(arr, k)

def array_of_array_products(arr):
    """
    - integer
    - duplicates
    
    arr = [8, 10, 2]
            [20, ]
            [20, 16, 80]
    
    Idea #1 - quadratic, another array - O(n^2), O(n)
    
    
    # init another array
    # output = [0 for _ in range(arr)]  # [0 , 0, 0]
    output = list()
    if len(arr) > 1:
        # populate the second
        for output_index in range(len(arr)):
        product = 1
        for input_index, input_value in enumerate(arr):
            # iterate over all other indicies in input
            if output_index != input_index:
            # make the product
            product *= input_value
        # put it in the output array
        output.append(product)
    # return the array
    return output
    """
  
    # make an array filled with left side ansers
    left = list([1])
    for index in range(1, len(arr)):
        next_left = left[index - 1] * arr[index - 1]
        left.append(next_left)
    # modify the array to also account for the right side
    right = list([1 for _ in len(arr)])
    for index in range(len(right) - 2, 0, -1):
        next_right = arr[index + 1] * right[index + 1]
        right[index] = next_right
    # bring it all together
    output = list()
    for index in range(len(arr)):
        output.append(left[index] * right[index])
    return output


if __name__ == "__main__":
    print(array_of_array_products([]))
# start with 1 in the last, move back, fill each with +1 index in arr, multipled with +1 in out
  

"""
[2, 7, 3, 4]

[1, 2, 14, 42]




"""
  
  


"""

[8, -10, 2]

o  = [-20, 0, 0]

oi    |   ov     |    p    |   ii    |     iv    |
0         0           -20       2           2


___________________

Idea #2 - Memoization

- reduce re-muplication

[8, -10, 2]

[-20, 16, -80]
     ^
     
[1, 8, -80]  -- L p = 2
         ,-80 ]
 
[-20, 2, 1] -- R
 
 
____________________
     



________________________
n = len of array

[2, 7, 3, 4]
[
  (1, 2, 3),
  (0, 2 ,3),
  
]

[84, 24, 56, 42]

n - 1 ints


____________________




"""
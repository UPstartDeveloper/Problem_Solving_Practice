def get_permutations(input_list):
    # init the empty output array
    output = list()
    def generate_permuations(nums_left, permutation):
        # base case
        if len(permutation) == len(input_list):
            # add the num to the permutation
            # permutation.append(nums_left.pop())
            # append to the output
            output.append(permutation)
            return
        # Recursive Case:
        else:  # permutation is incomplete
            # for each of the remaining numbers
            for index in range(len(nums_left)):
                num = nums_left[index]
                # add it to the permuation so far
                permutation.append(num)
                # return the next recursive call (w/o next num)
                generate_permuations(nums_left, permutation)
            return None
    # init nums left = input_list
    nums_left = input_list
    # init the perm to an empty array
    perm = list()
    # find all permutations
    next_num_index = 0
    generate_permuations(nums_left, perm)
    # return the output
    return output
  
    
print(get_permutations([1,2,3]))

"""
init the output = [
  [1, 2,3]
]
1, 2, 3

              _ _ _
       /     
      1 _ _ [2, 3]
      /        \
    12, [3]
  /       |
1 2 3   132

# need a sequence to repr a single perm - list
# what numbers have been used in the perm so far - list
# need a way to make sure the permutations not repeated
# output 2d arr

# Base Case:
nums_left = [1]

sequence = []

output = [[1]]

recursive case: len(nums) > 1


"""
    
    
    
    
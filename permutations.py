import numpy as np 

def get_permutations(input_list):
    # init the empty output array
    global output 
    output = list()
    def get_remaining_nums(nums_left, index):
        """# calculate the amount of nums needed
        nums_required = len(input_list) - len(permutation)
        nums_taken, index = [], 0
        # begin searching for numbers
        while len(nums_taken) < nums_required:
            num = input_list[index]
            # decide to add the number or not
            if num not in permutation:
              nums_taken.append(num)
            # iterate the index
            index = (index + 1) % len(input_list)
        return nums_taken"""
        # make a deep copy of the array 
        # (so the changes made to one don't affect the other)
        remaining_nums = np.array(nums_left).copy()
        remaining_nums = list(remaining_nums)
        # remove the num just added, then return the rest
        remaining_nums.pop(index)
        return remaining_nums
    def generate_permutations(nums_left, permutation):
        # base case
        if len(permutation) == len(input_list):
            # add the num to the permutation
            # permutation.append(nums_left.pop())
            # append to the output
            print(f'appended {permutation} to the output: {output}')
            output.append(permutation)
            return
        # Recursive Case:
        else:  # permutation is incomplete
            # for each of the remaining numbers
            for index in range(len(nums_left)):
                print(f'At index {index} in array: {nums_left}')
                num = nums_left[index]
                # add it to the permuation so far
                permutation.append(num)
                print(f'Permutation: {permutation}')
                # return the next recursive call (w/o nums already added)
                # remaining_nums = get_remaining_nums(nums_left, permutation)
                remaining_nums = get_remaining_nums(nums_left, index)
                generate_permutations(remaining_nums, permutation)
                permutation.pop()
            return 
    # init the perm to an empty array
    perm = list()
    # find all permutations
    generate_permutations(input_list, perm)
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
    
    
    
    
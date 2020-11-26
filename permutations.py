import numpy as np 
class Solution:
    output = list()

    def get_permutations(self, input_list):
        # init the empty output array
        def get_remaining_nums(nums_left, index):
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
                next_perm = list(np.array(permutation).copy())
                self.output.append(next_perm)
                # print(f'appended {permutation} to the output: {self.output}')
                return
            # Recursive Case:
            else:  # permutation is incomplete
                # for each of the remaining numbers
                for index in range(len(nums_left)):
                    num = nums_left[index]
                    # add it to the permuation so far
                    permutation.append(num)
                    # return the next recursive call (w/o nums already added)
                    remaining_nums = get_remaining_nums(nums_left, index)
                    generate_permutations(remaining_nums, permutation)
                    permutation.pop()
        # init the perm to an empty array
        perm = list()
        # find all permutations
        generate_permutations(input_list, perm)
        return self.output
    
sol = Solution()
print(sol.get_permutations([1,2,3]))

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
    
    
    
    
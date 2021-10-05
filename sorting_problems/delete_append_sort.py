# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
# insight: the last element to DA (if it's out of order) is the max
def da_sort(nums):
    def is_sorted(nums):
        """Determine if the list of numbers is sorted."""
        for index in range(len(nums) - 1):
            element_before, element_after = nums[index], nums[index + 1]
            if element_before > element_after:
                return False
        return True

    def delete_and_append(index):
        # perform the DA operation
        nums.append(nums.pop(index))
        return None

    # init number of operations
    operations = 0
    # find the max number in the array
    maximum = max(nums)
    # perform DA operations as long as the list remains unsorted
    while is_sorted(nums) is False:
        # find the current index of the maximum
        max_index = nums.index(maximum)
        # find the indices of the elements out of order
        out_of_order = list()
        # iterate backwards through the array
        for index in range(len(nums) - 1, 0, -1):
            index_before = index - 1
            element_after, element_before = nums[index], nums[index_before]
            if element_after < element_before:
                # add index to the array
                out_of_order.append(index_before)
        # get the index of the last element out of order that we found
        last_out_of_order = out_of_order[0]
        # if the number of out-of-order > 1 and first index = max
        if len(out_of_order) > 1 and last_out_of_order == max_index:
            # perform the DA on the second index
            delete_and_append(out_of_order[1])
        else:  # otherwise just perform the DA on the first index
            delete_and_append(last_out_of_order)
        print(f"Current state: {nums}")
        # increment the number of operations performed
        operations += 1
    print(f"Sorting complete in {operations} steps.")
    return operations


if __name__ == "__main__":
    numbers = [1, 5, 2, 4, 3, 6]
    numbers = [38, 27, 43, 3, 9, 82, 10]
    da_sort(numbers)

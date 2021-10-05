def permutations(nums):
    """Given a list, return all the possible orderings in an array.
    3 ingredients to Backtracking:
        1. Goal - fill up a permutation
        2. choices - unused values of nums
        3. constraint - values that are already used
    """

    def find_permutations(current, remaining, found):
        """Computes the permuations in just 1 branch of the tree."""
        # base case - current perm is complete
        if len(current) == len(nums):
            found([num for num in current])
        # recursive cases
        elif len(current) < len(nums):
            # add each of the remaining nums to the current permutation
            for index in range(len(remaining)):
                current.append(remaining[index])
                # recurse
                new_remaining = [
                    rem_num
                    for rem_index, rem_num in enumerate(remaining)
                    if index != rem_index
                ]
                find_permutations(current, new_remaining, found)
                # remove the previously added num
                current.pop()

    # A: init a list to store all perms
    all = list()
    # B: traverse the tree of permutations - init the current perm
    find_permutations([], [num for num in nums], all.append)
    # C: return all the permutations found
    return all


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permutations(nums))

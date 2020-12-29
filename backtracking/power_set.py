"""
Power Set: Write a method to return all subsets of a set.

Clarifying questions: 
- so ok, let's start off with an example to make this clearer
- is the input modifiable? no

s = {5, 7, 6, -8, 9, 10}, right?

Assumptions about the set:
- unordered collection
- all unique elements
- elements can only be integers (positive or negative?)
- return the output in an array of sets

so from here, what would my output be?

Subsets of 1:
{5}, {7}, {6}, ...
Subsets of 2:
{5, 6}, {7,6}

- so it's basically every kind combination, given a size from 1 -> n?

Intuition:
- for each size in range 1 --> n:
    - backtrack through all the possible combinations
- return all the subsets in one array at the end

Edge case: 
- what if there's an empty set as an input?
    - then return an empty set
- can there be an nested elements?
    - assume there's none for now

Approach: backtracking

# A: init the list for the return value
# B: iterate over all possible sizes


Size: 3

set =  {5, 7, 6, -8, 9, 10},
subsets = {
    {5}, {7}, {6}, {-8} , {9}, {10}, - n iterations
    { 5 , 7 }, { 5 , 6 }, { 5 , -8} - n^2 iterations
    {5 7 6}
}
Subset = { _ , _ , _}

                    {5, 7, 6, -8, 9, 10}

                    _   _   _
                    /
                5 _ _
            /                        /
          5 6                          5 7      
                                    /  \       \       \ 
                            5 7 6  5 7 -8   5 7 9   5, 7 10

"""


def power_set(values):
    '''Return all the set of all subsets of a set.'''
    # A: init the set for the return value
    subsets = list()
    def size_subsets(size, current, values):
        '''Finds all subsets of a given size in a set.'''
        # Base Case: the current subset is full
        if len(current) == size:
            # add the current subset to the output (if not already there)
            current_set = set(current)
            if current_set not in subsets:
                subsets.append(current_set)
        # Recursive Case: need to find more values for the subset
        else:  # len(current) < size
            # iterate over adding the others
            for _ in range(len(values)):
                new_item = values.pop()
                print(f"Current and new item: {current, new_item}")
                 # add one more value to the current subset
                current.append(new_item)
                size_subsets(size, current, {v for v in values})
                print(f"Values left: {values}")
                # remove one of the elements, so we reach all possibilities
                current.pop()
        return None
    # B: iterate over all possible sizes
    for size in range(1, len(values) + 1):
        # add the subsets of the given size to the output
        size_subsets(size, [], {v for v in values})
    # C: return all the subsets
    return len(subsets)


"""
Time and Space: O(sum(n! / ((n - k)! k!)), where k goes from 1 to n)

values = 
{6, 7, 8}

ss = {
    {6},
}
size = 1

current =                                   []
                                    [], v = {7, 8}  
                                       [7], v = {8}               
"""


if __name__ == "__main__":
    # values = {5, 7, 6, -8, 9, 10}
    values = {6, 7, 8}
    # values = {}
    print(power_set(values))

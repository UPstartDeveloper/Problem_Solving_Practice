'''
Two-Sum
https://leetcode.com/problems/two-sum/

Description on LeetCode
"Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."

Restate problem
Okay, so I have a list of integers (means whole numbers) and a sum value
I'm trying to add up to - and my job is just to look for a pair of numbers
that add up to the sum, and return their indicies in the array?

Ask clarifying questions/State Assumptions
Is the array sorted? I assume not.
Can there be duplicated values in the array? I assume yes.
Is the array immutable, or am I allowed to change the elements? I assume so.
Is it possible to not find the pair? What should it return then?
I assume so, and in that case we should be returning an empty list.

Think out load - Brainstorm
Ok so I guess I can just start by  traversing through all the array elements
Actually if the arrays not sorted, I want to start by sorting it first, since
that will make, on each iteration through each number, searching for the OTHER
number faster, because I can use a divide and conquer strategy. Hmm, we're more
likely to find the other number near the end of the array, so we want a
strategy that disregards the elements we don't care for - why not use binary
search?

This will make it easier to look for the other element.

Here's the pseudocode then:

Sort the list (using the built-in, this take O(n) because Python uses TimSort)
Traverse the list (O(n))
    on each iteration, binary search for the other element (O(log n))

So we're looking at a runtime of O(n log n) - not great, but for now I honestly
don't see a better way. For now I'll implement it, and let's see a better
idea emerges, ok?
'''


def binary_search(array, other_num, low, high):
    """Searches for the other number needed to make the target sum.
       Returns array index, or -1 if not found.
       low and high - index positions between which we are searchig

    """
    mid = (low + high) // 2
    # base case - successful
    if array[mid] == other_num:
        return mid
    # base case - not successful
    elif low == high:
        return -1
    # recursive case - int too small, so move to upper half
    elif array[mid] < other_num:
        return binary_search(array, other_num, mid, high)
    # recursive case - int too large, so move to lower half
    elif array[mid] > other_num:
        return binary_search(array, other_num, low, mid)


def two_sum(array, target):
    '''Solution to the above problem.'''
    array.sort()  # sort the array
    pair = []  # init list to store indices
    for index in range(len(array)):
        num = array[index]
        # calculate the other number we need to make the target sum
        other_num = target - num
        # perform binary search on the rest of the array, supply low and high
        other_index = binary_search(array, other_num, 1, len(array))
        # if both indices valid, we found the pair!
        if not (other_index == -1 or other_index == index):
            pair = [index, other_index]
    return pair


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # it works!


'''
In terms of tradeoffs I do sacrifice a lot of time by sorting the list, and
that would become a real problem if this is used with a dataset of thousands
of items.

To improve it, might I suggest using a hash table instead? That way we could
avoid sorting, use a traversal to build a histogram of our numbers, and lookup
the other number need to make a pair in linear search (but at the same time
that may make it harder to return the index of the numbers).
'''

from typing import List

# Problem Description on Hacker Rank: http://hr.gs/3apgt

"""
Variable-Value Table:

num_swaps: 5

should_be_index: 4

minimum: 5

min_index: 5

      0  1  2  3  4  5  6
arr: [7, 1, 3, 2, 4, 5, 6]
     [1, 7, 3, 2, 4, 5, 6]
     [1, 2, 3, 7, 4, 5, 6]
     [1, 2, 3, 4, 7, 5, 6]
     [1, 2, 3, 4, 5, 7, 6]
     [1, 2, 3, 4, 5, 6, 7]

"""


def min_swaps(arr: List[int]):
    """Return the minimum number of swaps needed to sort a list in ascending
    order.

    arr(List[int]): a list of positive integers. No duplicates.
                    Once sorted, all the elements are consecutive.

    Return: int: the lowest number of swap operations needed to sort arr

    """

    def swap(index1: int, index2: int):
        """Performs a mutative swap on the array."""
        arr[index1], arr[index2] = arr[index2], arr[index1]
        return None

    # initialize a counter for amount of swaps
    num_swaps = 0
    # pointer for what index the lowest index should be in
    should_be_index = 0
    # determine if the list is unsorted
    while arr != sorted(arr):  # while loop for now, but might work as for?
        # track what the value and index of lowest is
        minimum = min(arr[should_be_index:])
        min_index = arr.index(minimum)
        # if not where it should be, swap the indices
        if min_index != should_be_index:
            swap(min_index, should_be_index)
            # increment the swaps
            num_swaps += 1
        # on next iteration, the lowest should go in the next index
        should_be_index += 1
    return num_swaps


if __name__ == "__main__":
    arr = [7, 1, 3, 2, 4, 5, 6]
    print(min_swaps(arr))

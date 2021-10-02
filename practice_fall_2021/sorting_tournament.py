from typing import List

def bubble_sort(nums) -> List[int]:
    """Sorts numbers from in ascending order.
    It is:
        - quadratic time
        - constant space
        - stable
        - iterative
        - mutative
        - internal algorithm
    """
    # TODO: implement the algorithm!
    pass


def insertion_sort(nums) -> List[int]:
    """TODO: describe this algorithm using CS knowledge"""
    # TODO: implement the algorithm!
    pass


def merge_sort(nums) -> List[int]:
    """TODO: describe this algorithm using CS knowledge"""
    # TODO: implement the algorithm!
    pass


def quick_sort(nums) -> List[int]:
    """TODO: describe this algorithm using CS knowledge"""
    # TODO: implement the algorithm!
    pass


if __name__ == "__main__":
    test_cases = [
        # in the order: (Input, Expected Output)
        # 1) Random order (aka avg case)
        ([2, 1, 3, -7, 4, 6, -3], [-7, -3, 1, 2, 3, 4, 6]),
        # 2) Nearly Sorted
        ([1, 2, 4, 5, 6, 7, -8], [-8, 1, 2, 4, 5, 6, 7]),
        # 3) Reversed order
        ([8, 7, 6, 5, 4, 3, -1], [-1, 3, 4, 5, 6, 7, 8]),
        # 4) Few Unique order
        ([2, 2, 2, 45, 5, 5, 1], [1, 2, 2, 2, 5, 5, 45])
    ]

    #### TODO: test out your algorithms on the test cases!

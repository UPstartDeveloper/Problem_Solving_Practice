from collections.abc import Iterable
from typing import Tuple


class Solution:
    def __init__(self):
        self.count = 0

    def count_tuple_elements(self, elements: Tuple[str, int], target: int) -> int:
        """
        Problem (from InterviewQs):
            Suppose you are given a tuple containing ints and strings.
            Write a Python function to return
                the # of times a given element, n, appears in the tuple.

            For example, given the tuple below,
            where n=3,
            your function should return 4,
            since 3 appears 4 times in the tuple.

        input: n = 3
               my_tuple = 2, 'my_string', 4, 3, 3, 3, 2, 3
        output: 4

        ASSUME tuple is not empty
        DO NOT ASSUME if it is 1D or not

        Intuition:
            recursive
            linear search

        EC:
            jagged ndim tuple --> should handle
            item not in the tuple at all --> 0

        Approach: this problem requires a flow chart

        """
        ### HELPER
        def _count_freq_of_target(target, elements, index=0):
            if index < len(elements):
                elem = elements[index]
                # recursive
                if isinstance(elem, Iterable) and not isinstance(elem, str):
                    _count_freq_of_target(target, elem)
                # base case
                elif elem == target:
                    self.count += 1
                # move on
                return _count_freq_of_target(target, elements, index=index + 1)
            # all done!
            return self.count

        ### MAIN
        self.count = 0  # reset to zero at the start of each invocation
        return _count_freq_of_target(target, elements)


if __name__ == "__main__":
    solver, target = Solution(), 3
    # TEST: empty tuple
    test1 = ()
    assert solver.count_tuple_elements(test1, target) == 0
    # TEST: 1D tuple
    test2 = (2, "my_string", 4, 3, 3, 3, 2, 3)
    assert solver.count_tuple_elements(test2, target) == 4
    # TEST: 2D tuple
    test3 = (
        (2, "my_string", 4, 3, 3, 3, 2, 3),
        (2, "my_string", 4, 3, 3, 3, 2, 3),
    )
    exp, actual = 8, solver.count_tuple_elements(test3, target)
    assert exp == actual, f"Expected {exp}, actually got {actual}"
    # TEST: 2D tuple (jagged)
    test4 = (
        (2, "my_string", 4, 3, 3, 3, 2, 3),
        (2, "my_string", 3, 3, 2, 3),
    )
    assert solver.count_tuple_elements(test4, target) == 7
    # TEST: nested tuples (jagged)
    test5 = (
        (2, "my_string", 4, 3, 3, 3, 2, 3),
        (2, (6, 7, 3), 3, 3, 2, 3),
    )
    assert solver.count_tuple_elements(test5, target) == 8

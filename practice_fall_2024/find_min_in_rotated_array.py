class Solution:
    """https://neetcode.io/problems/find-minimum-in-rotated-sorted-array"""
    def find_min(self, nums: list[int]) -> int:
        """
        Input
            nums: list[int]
                immutable
                constrained range - pos/neg
                dupes posible
                non-empty

        Output: min value

        Intuition
            search (ideally using binary search)

        BCR
            O(log n)
            O(1) space

        Approaches

        [3,4,5,6,1,2]
         ^         ^
                 ^
         3 > 2
         6 > 2
         1 < 2

            1. Brute force - linear search

            2. Binary Search - iterative, O(1) space
                given target + sorted arr - cuts half of search space
                recursive
                    subproblem: sub array
                        init l, hi, m = (l + hi) // 2
                        base case:
                            low == hi
                                min is found!

                        recursive case:

                            low < hi
                                recurse on left side

                            low > hi
                                recurse on right side
                 0 1 2 3 4 5
                     m
                       m
                [4,5,0,1,2,3]
                 ^.        ^
                 0         5
                     ^.    ^
                     2.    5
                     ^ ^
                     2 3
                     ^
                 4 > 3
                 0 < 3
                 0 < 1
                 0 == 0
         0.1 2 3 4
        [5,1,2,3,4]
         ^.      ^
             ^.^
             ^
        """
        ### HELPER(S)
        def _binary_search_iterative():
            low, hi = 0, len(nums) - 1

            while low < hi:
                # capture the edge cases
                if low < len(nums) - 1 and nums[low + 1] < nums[low]:
                    low = low + 1
                if hi > 1 and nums[hi - 1] < nums[hi]:
                    hi = hi - 1

                # continue the binary search
                mid = (low + hi) // 2
                if nums[low] < nums[hi]:
                    # recurse on the left to get closer to min
                    hi = mid

                elif nums[low] > nums[hi]:
                    # recurse on the right to get closer to min
                    low = mid

             # min found
            return nums[low]

        ### DRIVER
        return _binary_search_iterative()

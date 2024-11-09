class Solution:
    """https://neetcode.io/problems/duplicate-integer"""
    def has_duplicate(self, nums: list[int]) -> bool:
        """
        Problem:
            duplicate detection

        Test Cases:
            list[int]

            [] --> true
            pos and neg possible
            not sorted?

        Assumptions
            array might not be sorted
            array size will fit in memory

        Intuition
            easiest ---> use hashing

        Approach

            BCR --> O(n)
            best possible storage --> O(1)?

            1. Brute force
                iter8 over array
                place each item in a set
                if any item already in --> false
                else true

                Time: O(n)
                Space: O(n)

            2. If already sorted:
                do a linear search over array
                use 2 pointers - compare adj elems to check they're !=

                Time: O(n)
                Space: O(1)

            3. if not sorted:
                sort it --> since all ints, use:
                    TimSort ---> O(n log n)
                    Counting Sort --> O(n + k)

                then do the linear pass above
        """
        ### DRIVER
        # iter8 over array, use set to detect dupes
        return len(set(nums)) != len(nums)

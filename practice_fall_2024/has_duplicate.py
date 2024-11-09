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

        Test case:
            cni
            0, 1, 2, 4

            min_elem
            1

            max_e
            3
                      0  1  2
            counts = [1, 1, 2]
                      ^
            nums
            [1, 2, 3, 3]
             ^

             count = 1

        """
        ### HELPERS
        def _using_set() -> bool:
            return len(set(nums)) != len(nums)

        def _using_sort() -> bool:
            has_dupe = False

            # sort using counting sort
            min_elem = min(nums)
            max_elem = max(nums)

            # init counts array
            counts = [0 for _ in range(max_elem - min_elem + 1)]
            # diff = max_elem - min_elem

            # populate the counts - TODO[test]
            for num in nums:
                counts[num - min_elem] += 1

            # sort the array
            current_nums_index = 0

            for index, count in enumerate(counts):
                value = index + min_elem  # 2 + 1 = 3

                for nums_index in range(current_nums_index, current_nums_index + count): # (2, 3)
                    nums[nums_index] = value

                current_nums_index += count

            for index1 in range(len(nums) - 1):
                index2 = index1 + 1

                num1, num2 = nums[index1], nums[index2]

                if num1 == num2:
                    has_dupe = True
                    break

            return has_dupe


            # pass over array to find a duplicate
        ### DRIVER
        # iter8 over array, use set to detect dupes
        return len(set(nums)) != len(nums)

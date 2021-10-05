class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Input/Problem:
            pos/neg ints
            ASSUME fits in mem
            CAN have an empty array
            dupes
            unsorted
            ASSUME not immutable

        - out: 2D int ---> all poss triplets (elems) sum() == 0

        Clarify:
            - repeats allowe ACROSS, but not inside a triple
            - can NOT have exact same triplets (even if using different elems)

        EC:
            1) < 3 values ---> []
            2) TODO

        Intuition:

        [-1,0,1,2,-1,-4]

        A: [-1,0,1,2,-1,-4] --> [-4, -1, -1 ,0, 1, 2]
        B:                                1st ^ ^

        [[-1, 0, 1], [-1, -1, 2]]

            1) 1Sum: linear search for 0 (1 pter)
                2) 2Sum: 2 pointers (nested for loops) - sum to first number
            3) 3Sum: 3 pters

        Open Question:
            1) how to avoid dupe triplets?
                - idea: only 2Sum for the REST of array (pointer move into center)
        Approach:
            1) sort the array first - nlogn
            2) 1Sum n iterations
                a) 2Sum  n^2
        """
        ### HELPERS
        def _is_all_zeros():
            for num in nums:
                if num != 0:
                    return False
            return True

        def _search_2sum(index1, target):
            """gets all pairs of numms that sums to target,
            in the range of index1 + 1, len(nums) - 1] in the list.
            modified iterative binary search"""
            pairs = list()
            for increment in range(1, len(nums) - index1):
                index2, index3 = index1 + increment, len(nums) - 1
                while index2 < index3:
                    pair = nums[index2] + nums[index3]
                    # lower
                    if pair < target:
                        index2 += 1
                    # higher
                    elif pair > target:
                        index3 -= 1
                    # target found
                    else:  # pair == target:
                        pairs.append([nums[index2], nums[index3]])
                        index2 = index3  # break the loop
            # target not found
            return pairs

        ### DRIVER
        # special case:
        if len(nums) > 2 and _is_all_zeros():
            return [[0, 0, 0]]
        # A: sort the array
        triplets, seen = list(), set()
        nums.sort()
        # B: 1Sum problem
        for index1 in range(0, len(nums) - 2):
            first = nums[index1]
            # C: binary search of the 2Sum problem
            pairs = _search_2sum(index1, -1 * first)
            for p in pairs:
                second, third = p
                triplet = (first, second, third)
                if triplet not in seen:
                    triplets.append(triplet)
                    seen.add(triplet)
        # D: return output
        return triplets

class Solution:
    """https://neetcode.io/problems/buy-and-sell-crypto"""
    def maxProfit(self, prices: list[int]) -> int:
        """
        Input(s):
            prices
                non-empty
                mutable? probably is not, don't need edits
                unsorted
                dupes possible
                non-negatives

        Output
            int - greatest inc between any 2 ints

        Intution
            DP?
            2 pter solution?

        EC:
            all decreasing --> 0
            all increasing (aka sorted) --> diff(max, min) - 2 ends of array
            all the same --> 0

        BCR
            O(n)

        Approach:

            1) Brute Force - nested loops
                O(n^2), O(1) space

                for each elem
                    find the highest val in arr after it
                    take the diff
                    see if it's the highest diff so far
                return highest diff

            2) "Linear Search"?

                - observations
                    - never buy on the day of the max

                    1 ->
                [10,1,5,6,7,1]
                        <- 2

                 [10,1,5,6,7,1]
                      ^      ^
                diff = -9
                        4
                        5
                        6
                        0
                 [10,8,7,5,2]
                         ^ ^

                diff
                    = -7
                    = -1
                    = -2
                    = -3

                A: init 2 pointers and largest_diff = 0

                B: while both pters in range of the list

                    a: check the values
                        i. if the diff < 0
                            move both pointers + 1
                        ii. if the diff >= 0
                            calc the prof
                            update largest_diff if appropiate

                    b: if the value after latter ptr is higher than ptr1:
                        move ptr2

                    c: else:
                        move ptr1 to after ptr2, and ptr2 to ptr1 + 1

                C: return largest_diff
        """
        ### Check EC
        if len(prices) < 2:
            return 0
        ### DRIVER
        # A: init 2 pointers
        largest_diff = 0
        ptr1, ptr2 = 0, 1

        # B: while both pters in range of the list
        while ptr1 < len(prices) and ptr2 < len(prices):
            # a: check the values
            if prices[ptr1] > prices[ptr2]:
                ptr1 += 1
                ptr2 += 1
            # update largest_diff if appropiate
            elif prices[ptr1] <= prices[ptr2]:
                largest_diff = max(largest_diff, prices[ptr2] - prices[ptr1])

                # b: if the value after latter ptr is higher than ptr1:
                if ptr2 < len(prices) - 1 and prices[ptr2 + 1] >= prices[ptr1]:
                    ptr2 += 1
                else:
                    ptr1 = ptr2 + 1
                    ptr2 = ptr1 + 1

        return largest_diff

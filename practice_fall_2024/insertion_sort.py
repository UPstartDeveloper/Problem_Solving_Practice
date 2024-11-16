#!/usr/bin/python3

class Pair:
    """# Definition for a pair."""
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    """https://neetcode.io/problems/insertionSort"""
    def insertion_sort(self, pairs: list[Pair]) -> list[list[Pair]]:
        """
        Intuition: insertion sort
            stable
            in-place
            quadratic - n passes through the list
                take an element from the end,
                swap it down the list towards the sorted portion

        Constraints
            sorting by the key
            <= 100 - fit in memory

        output = [
            [(5, "apple"), (2, "banana"), (9, "cherry")]
            [(2, "banana"), (5, "apple"), (9, "cherry")]
            [(2, "banana"), (5, "apple"), (9, "cherry")]
             ^e

        ]
         is_sorted = False

         eosp = -1

        Approach:

            Idea 1 - modified insertion sort

            A: init output = []

            B: enter insertion sort of algo

                is_sorted = False

                enter a loop

                    end_of_unsorted_portion_index = eosp = pairs.length - 1
                    look at value @ eosp

                    enter nested loop -->
                        while value hasn't reached beginning,
                        keep swapping if possible


                        swap --> if last_elem < prior_elem then swap

                    output.add(copy of modified pairs as-is)
                    end_of_unsorted_portion_index -= 1

                is_sorted = True

            C: exit by returning pairs

        """
        ### HELPER(S)


        ### DRIVER
        # A: init output = []
        output = []

        # B: enter insertion sort of algo
        end_of_unsorted_portion_index = eosp = 0

        while eosp < len(pairs):

            # look at value @ eosp
            element_to_sort = ets = pairs[eosp]
            current_index = eosp

            # while value hasn't reached beginning, keep swapping if possible
            while current_index > 0 and ets.key < pairs[current_index - 1].key:

                # swap --> if last_elem < prior_elem then swap
                pairs[current_index], pairs[current_index - 1] = (
                    pairs[current_index - 1],
                    ets
                )
                current_index -= 1

            # output.add(copy of modified pairs as-is)
            output.append(pairs.copy())

            eosp += 1

        # C: exit by returning output
        return output


if __name__ == "__main__":
    #### TEST CASES

    # 1) normal input
    pairs1 = [Pair(3, "cat"), Pair(3, "bird"), Pair(2, "dog")]
    print(Solution().insertion_sort(pairs1))

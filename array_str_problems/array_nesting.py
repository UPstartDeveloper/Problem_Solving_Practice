from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/array-nesting/

        Input/Problem:
            n int >= 0
            range [0, n -1]
            no dupes
            unsorted
            immutable
            n >= 1

        Output:
            longest length poss for a set

        Intuition:
            maximize the diff(index, value) for 1st value

        EC:
            - OOM - assume not
            -

        Approach:
            1). Brute Froce
                A: init longest_length
                B: try every poss set (iter k through indices)
                    C: measure the resulting length - up to n iter
                D: return longest_length

             2) TODO: use DFS
                A: form a directed graph (vertex has an index, edge is to the index of its corr. elem)
                B: DFS/BFS each graph, return its size
                C: return size of largest component
        """
        ### HELPERS
        def _generate_set(index, current_set):
            # A: validate the index
            if index < len(nums):
                next_num = nums[index]
                # B: Recursive: not already in the set
                if next_num not in current_set:
                    current_set.add(next_num)
                    return _generate_set(next_num, current_set)
            # C: Base case: num already in
            return current_set

        ### DRIVER
        # A: init longest_length
        longest_length = ll = float("-inf")
        # B: try every poss set (iter k through indices)
        for starting_index in range(len(nums)):
            # C: measure the resulting length - up to n iter
            nums_set = _generate_set(starting_index, set())
            if len(nums_set) > ll:
                ll = len(nums_set)
        # D: return longest_length
        return ll

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
        
        Input:
            rectangular int[][bits, sorted, immutable, non-empty]
            k = int
            stable sorting algorithm

        Output:
            sorted by most weakest --> [row_indices]

        Intuition:
            search
            sorting
            heaps

        Edge Cases:
            - [[]] or [] --> []
            - TODO

        Approach:

            1) Brute - quadratic approach:
                nested for loops --?
                    compare each row to every other
                    grant pts to the stronger row (hash table)

                sort the hash table

                pull the k weakest

            2) Optimal - {# solder --> [row_indices]} 
                A: map {# soldier --> [row_indices]}
                B: traverse the key-value pairs in sorted order
                    C: return the first k

        """
        ### HELPERS
        def _get_soldiers_of_rows(mat):
            """map {unique # soldier --> [row_indices]} - 2D array"""
            soldiers_of_rows = [list() for _ in range(len(mat[0]) + 1)]  # n iter
            for index, row in enumerate(mat):  # m iterations
                num_soldiers = _count_soldiers(row)  # log(n) iterations
                # add the row index as a value to a new/existing key
                soldiers_of_rows[num_soldiers].append(index)
            return soldiers_of_rows

        def _count_soldiers(row):
            """find the 1st civillian - binary search"""
            lo, hi = 0, len(row)
            while lo <= hi:
                mid = (lo + hi) // 2
                if mid < len(row):
                    found = row[mid]
                else:  # there are no zeros in the row
                    break
                # move to next sub problem
                if found == 0:
                    # Base case: verify it's the first 0
                    if (mid == 0) or (mid > 0 and row[mid - 1] == 1):
                        break
                    # Recursive case: go left
                    else:
                        hi = mid - 1
                # Recursive case: go right
                elif found == 1:
                    lo = mid + 1
            return mid

        ### DRIVER
        # A: map {# soldier --> [row_indices]}
        soldiers_of_rows = _get_soldiers_of_rows(mat)  # O(m * log(n))
        # B: traverse the key-value pairs in sorted order
        weakest = w = list()
        for row_indices in soldiers_of_rows:  # n iteration
            # adding rows to output
            for index in row_indices:  # k iter
                if len(w) < k:
                    w.append(index)
                else:
                    break
        # C: return the first k
        return w


# Time: O(m * log(n))
# Space: O(n * m)

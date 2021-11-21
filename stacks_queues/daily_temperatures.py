from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/daily-temperatures/

        Input/Problem:
            immutable
            arr[int]
            pos
            dupes

        Output:
            distance from each temp ----> index of value > temp, right

        Intuition:
            dynamic programming
            greatest value in array ---> answer[i] = 0

        EC:
            1. invalid - empty, out of range ---> ValueError
            2. TODO

        Approach:
            1) Brute force - repeated linear searches - quadratic
            2) Right to left - TODO
                last index -----> 0 in answers
                index of great ----> 0 in answers

                         g
          0. 1  2. 3. 4. 5. 6. 7
        [73,74,75,71,69,72,76,73]
                  ^
                4  2  1  1  0  0

        A: linear search -----> find the greatest value
        B: pop. answers = [], traverse temp in reverse, using current
            1) last index -----> 0 in answers
            2) index of great ----> 0 in answers
            3) if temp[current] < temp[greatest] and current < greatest:
                answer = greatest - current
            4) move greatest pointer
                if current - 1 < current ----> greatest = current
                else ---> greatest += 1 until temp[greatest] > temp[current - 1]

        """
        ### HELPER
        def _find_answer(index, temp):
            greater_ndx = gn = index + 1
            while gn < len(temperatures) and temperatures[gn] <= temperatures[index]:
                gn += 1
            if gn < len(temperatures):
                return gn - index
            return 0

        ### DRIVER
        # A: init answers
        ans = list()
        # B: populate answers
        for index, temp in enumerate(temperatures):
            ans.append(_find_answer(index, temp))
        # C: all done!
        return ans


"""
t = [30,60,90]
           ^ g
a = [1, 1, 0]

"""

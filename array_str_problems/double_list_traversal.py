from typing import List, Tuple


class Solution:
    def count_using_two(nums: List[int]) -> Tuple[int, int]:
        sum1, sum2 = 0, 0
        for index1 in range(0, len(nums) - 1, 2):
            index2 = index1 + 1
            sum1 += nums[index1]
            sum2 += nums[index2]
        return sum1, sum2

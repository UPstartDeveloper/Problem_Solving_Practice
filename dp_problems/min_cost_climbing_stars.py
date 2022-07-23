from collections import List


class Solution:
    def __init__(self):
        self.cache = dict()  # index --> ssf

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        LeetCode: https://leetcode.com/problems/min-cost-climbing-stairs/
        
        Intuition:
            cheapy algo - trying to min a local cond
            
        EC: 
            len(nums) < 2 --> ValueError
            neg - ValueError
            sorted - fine
            dupes - fine
            unsorted - fine
            0 - fine
            
        Output:
            int: min(sum of steps taken)
            
        Approach:
            
            Reverse Traversal
            
                A) init pointer = n, and ssf = 0
                
                B) while pter > 1:
                    
                    look at last two
                    choose smaller to update ssf
                    move back the pter to the smaller
                
                C) return ssf
            
        """
        ### HELPERS
        def _get_sum(index):
            # Base Case: out of array
            if index >= len(cost):
                return 0

            # Recursive - get the min of both possible 'next' options
            elif index not in self.cache:
                c = cost[index]
                self.cache[index] = min(
                    c + _get_sum(index + 1), c + _get_sum(index + 2)
                )

            return self.cache[index]

        ### EC:
        nums = cost
        if not isinstance(nums, list) or len(nums) < 2:
            raise ValueError(f"Expected int[] with len() > 1, actial is {nums}.")

        ### DRIVER
        sum1, sum2 = _get_sum(0), _get_sum(1)
        return min(sum1, sum2)

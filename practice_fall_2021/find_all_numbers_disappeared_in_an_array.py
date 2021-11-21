class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Leetcode link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"""
        # A: linear time, linear space
        return list(set(range(1, len(nums) + 1)) - set(nums))
        # B: linear time, constant space - TODO
        pass

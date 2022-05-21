class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ### HELPER
        def _recursive_helper(index):
            # base case:
            if index == len(nums) - 1:
                self.is_possible = True
                return
            
            # recursive
            elif index < len(nums):
                for new_index in range(
                    index + nums[index], index, -1
                ):
                    if not self.is_possible:
                        _recursive_helper(new_index)
                    else:
                        break
        
        ### DRIVER
        if len(nums) == 1:
            return True
        self.is_possible = False
        for new_index in range(nums[0], 0, -1):
            if not self.is_possible:
                _recursive_helper(new_index)
            else:
                break
        return self.is_possible

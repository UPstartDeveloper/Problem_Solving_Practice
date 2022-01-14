from typing import List


class Permutations:
    def permute_array(self, nums: List[int]) -> List[List[int]]:
        ### HELPERS
        def _backtracking_helper(current, all, choices):
            # Base: 1 perm done
            if len(current) == len(nums):
                all.append(current[:])
                return
            # Recursive: keep going if len(current) < len(nums):
            for index, num in enumerate(choices):
                current.append(num)
                remaining = [
                    n for other_ndx, n in enumerate(choices) if index != other_ndx
                ]
                _backtracking_helper(current, all, remaining)
                current.pop()
            return all

        ### MAIN
        return _backtracking_helper([], [], nums)


if __name__ == "__main__":
    nums = [10, 14, 15]
    solver = Permutations()
    print(solver.permute_array(nums))

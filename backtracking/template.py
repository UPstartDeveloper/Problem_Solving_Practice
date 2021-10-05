from typing import List, Set, Optional


class BackTracking:
    """choices (immutable), goal, constraint"""

    def __init__(self, choices: List[int]):
        self.choices = choices
        self.all_permutations = self.ap = list()

    def __call__(
        self, choices=None, current_perm: Optional[List[int]] = None
    ) -> Set[int]:
        """return the set of all permutations, given the choices"""
        # Init case
        if choices is None:
            return self.__call__(self.choices[:], current_perm=list())
        # Base Case: new perm found
        elif len(choices) == 0:
            self.ap.append(current_perm[:])
            return
        # Recursive: new perm is being made
        for index in range(len(choices)):
            item = choices[index]
            new_choices = [
                item for item_index, item in enumerate(choices) if index != item_index
            ]
            current_perm.append(item)
            self.__call__(new_choices, current_perm)
            current_perm.pop()
        return self.all_permutations


if __name__ == "__main__":
    # permutate an array of integers
    nums = [1, 2, 3]
    bt = BackTracking(nums)
    print(bt())

from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Leetcode link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
        Input/Problem:
            - binary tree
            - decimal vals > 0
            - ASSUME !empty
            - Output:
                - find all the R2L values
                - summation(R2L)

        EC:
            1) leaf - different depths
            2) only one node = return the root.val itself

        Intuition:
            pre-order DFS
                - store the digits for 1 R2L --> [10 vals]
                - decode the array ----> decimal
                - total += R2L

        Approach:
            1) DFS - linear time, constant space (b/c can assume is only up to 10)
        """
        ### HELPER
        def _decode(digits: List[int]):
            """[1, 2, 3] --> 123"
                      ^
                10^2
            iterate over the array
            """
            decoded_val = 0
            # - decode the array ----> decimal
            for index, digit in enumerate(digits):
                exp = len(digits) - 1 - index
                power = 10 ** exp
                decoded_val += digit * power
            return decoded_val

        def find_r2ls(node: TreeNode, digits: List[int], total_sum: int):
            # visit
            if node is not None:  # TODO: extraneous code
                digits.append(node.val)
                # Base case: R2L is found!
                if node.left is None and node.right is None:
                    total_sum += _decode(digits)
                # recurse on the left child
                if node.left:
                    total_sum = find_r2ls(node.left, digits, total_sum)
                    digits.pop()  # TODO: test!!
                # recurse on the right side
                if node.right:
                    total_sum = find_r2ls(node.right, digits, total_sum)
                    digits.pop()
            return total_sum

        ### DRIVER
        # DFS solution
        return find_r2ls(root, [], 0)

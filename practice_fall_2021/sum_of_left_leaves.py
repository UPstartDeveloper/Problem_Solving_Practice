from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Leetcode link: https://leetcode.com/problems/sum-of-left-leaves/
        assume at least 1 node (root is not null)
        node values are pos/neg ints
        """

        def _left_sum(current_sum, node):
            """recursive in-order DFS"""
            if node:
                current_sum = _left_sum(current_sum, node.left)
                # visit
                if node.left and node.left.left is None and node.left.right is None:
                    current_sum += node.left.val
                current_sum = _left_sum(current_sum, node.right)
            return current_sum

        return _left_sum(0, root)

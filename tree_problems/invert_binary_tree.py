from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Leetcode link: https://leetcode.com/problems/invert-binary-tree/
        Input/Problem:
            binary tree
            ASSUME input is a perfect tree
            ASSUME input is mutable

            Output:
                subproblem: node has reversed its subtrees

        EC:
            1) null root --> return root as it is
            2) not a full tree --> TODO
            3) not a complete tree --> TODO

        Intuition:
            node.left, node.right = node.right, node.left

        Approach:
            recursive in order DFS
                "visit" --> node.left, node.right = node.right, node.left

        """
        ### HELPER
        def _invert_binary_tree(node):
            """recursive preorder DFS to reverse subtrees"""
            if node is not None:
                # visit the current node
                node.left, node.right = node.right, node.left
                # visit left
                _invert_binary_tree(node.left)
                # visit right
                _invert_binary_tree(node.right)

        ### DRIVER
        if root is not None:
            _invert_binary_tree(root)
        return root

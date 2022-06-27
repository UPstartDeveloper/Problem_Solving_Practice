from typing import Optional 

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        LeetCode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
        Do not return anything, modify root in-place instead.
        """
        ### HELPERS
        def _flatten_helper(node):
            '''recursive postorder traversal'''
            if node:
                # recursive: 1 or 2 kids
                last_leaf = None
                temp = node.right
                if node.left:
                    # recurse(left)
                    last_leaf = _flatten_helper(node.left)
                    node.right = node.left
                    last_leaf.right = temp
                    # "null out" the left subtree
                    node.left = None
                
                # recurse(right)
                if temp:
                    return _flatten_helper(temp)
                
                # visit the node - decide what to return
                elif last_leaf:
                    return last_leaf
                else:  # this is a base case (i.e. when we visit a leaf)
                    return node

        ### DRIVER
        if root:
            _ = _flatten_helper(root)
        return root

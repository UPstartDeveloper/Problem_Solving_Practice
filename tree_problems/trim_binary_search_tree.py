from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        LeetCode:
            https://leetcode.com/problems/trim-a-binary-search-tree/
 
        Intuition
            preorder DFS, recursive, m utative
            
        Stepping Stone
            to cut out one node:
                root:
                    move root to the appropiate subtree
                general:
                    parent.child = child.child 
                        (need to choose child.child in range, or None)
                    then if the new parent.child is not None, recurse
                
        Approach:
            A: find the root of the trimmed tree first
            B: trim nodes
            C: return the new node
        
        """
        ### HELPERS
        def _find_root(node):
            if node:
                if node.val < low:
                    return _find_root(node.right)
                elif node.val > high:
                    return _find_root(node.left)
                elif low <= node.val <= high:
                    return node
        
        def _trim(node):
            if node:
                # figure out which children to keep
                if node.left:
                    node.left = _find_root(node.left)
                _trim(node.left)
                # do the same on th right side
                if node.right:
                    node.right = _find_root(node.right)
                _trim(node.right)
        
        ### DRIVER
        # A
        root = _find_root(root)
        # B
        _trim(root)  # assuming this (possibly new) root is valid
        # C
        return root
        

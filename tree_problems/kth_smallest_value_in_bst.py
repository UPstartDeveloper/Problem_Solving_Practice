from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
        
        Intuition:
            in order DFS
            sorting
            
        Assume:
            k <= n
            both are pos
            
        EC:
            null root --> raise ValueError
            invalid tree --> N/A
            
        Approach:
            do k visits in DFS
                on the kth visit, return
        
        """
        ### HELPERS
        def _find_kth_smallest(node, visits=0):
            """in-order DFS, recursively"""
            if node and visits < k:
                visits = _find_kth_smallest(node.left, visits)
                # visit
                visits += 1
                if visits == k:
                    self.kth = node.val
                if visits < k:
                    visits = _find_kth_smallest(node.right, visits)
            return visits

        ### DRIVER
        # A: init return value
        self.kth = -1
        # B: find kth-smallest
        if root:
            _find_kth_smallest(root)
        # C: return
        return self.kth

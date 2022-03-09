from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        Input:
            binary tree
            cannot assume complete, full
            pos/neg
            dupes
            null root possible
            tilt = abs(sum(left) - sum(right))
            
        Output:
            sum(tilt of all nodes)
            
        Intuition:
            post-order DFS
            
        Approach
        
            1) DFS ---> O(n) time, O(n) space
                init tilt = 0
                DFS
                    recurse on left, return sum of all left subtree values (add node val + its left and right)
                    do same on the right
                    tilt += abs(sum(left) - sum(right))
                return tilt
                
        EC: TODO
            1. null root ==> return 0
            
        Test:
            tilt = 0, 0, 0, 1
            
            node = root = 1,    left = 2,   right = 3
            node = 2,       left = 0,       right = 0
            node = 3,       left = 0,       right = 0
        =========================================================== 
        tilt_sum = 0 
        
        
        
        (2)         0
        (1)
        node        left_sum        right_   
        """
        ### HELPERS
        def _compute_tilt(node):
            '''post-order DFS'''
            # Recursive case
            if node is not None:
                # recurse on left, return sum of all left subtree values
                left_sum = _compute_tilt(node.left)
                #  do same on the right
                right_sum = _compute_tilt(node.right)
                # tilt of this node
                self.tilt_sum += abs(left_sum - right_sum)
                return node.val + left_sum + right_sum
            # base case
            return 0
        
        ### MAIN
        # init tilt
        self.tilt_sum = 0
        if root is not None:
            # DFS
            _compute_tilt(root)
        return self.tilt_sum

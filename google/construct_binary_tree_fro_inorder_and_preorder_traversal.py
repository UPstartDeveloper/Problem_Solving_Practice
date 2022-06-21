from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        WORK IN PROGRESS
        
        LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        
        pre:  root, left, righht
        in:   left, root, right 
        
        
        1) find root --> from preorder (1st elem)
        2) find left subtree:
            in the inorder travesal BEFORE the root
            
        3) find right subtree:
        
                    r l rr
        preorder = [3,9,20,15,7], 
        
                    l r    
         inorder = [9,3,
                             l r  rr
                            15,20,7]
        
        Approach:
            Subproblems:
                
                
        """
        ### HELPERS
        def _index(array, elem):
            for index, val in enumerate(array):
                if val == elem:
                    return index
            return -1
        
        def _construct_imbalanced(preorder):
            root = TreeNode(preorder[0])
            node = root
            for idx in range(1, len(preorder)):
                node.right = TreeNode(preorder[idx])
                node = node.right
            return root

        def _construct_tree(preorder, inorder) -> Optional[TreeNode]:
            # base case
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            
            # recursive case
            root_val = preorder[0]
            root_val_index = _index(inorder, root_val)
            root = TreeNode(root_val)
            
            # potential nodes for (left, root, right)
            candidate_node_vals = inorder[root_val_index - 1:root_val_index + 2]
                
            # do the left subtree, if there is one
            if root_val_index > 0 and len(preorder) > 1:
                left_subtree_index = _index(inorder, preorder[1]) 
                if left_subtree_index > -1:
                    root.left = _construct_tree(
                        preorder[1:], inorder[:root_val_index]
                    )

            # do the right subtree
            preorder_index = float("inf")
            if not root.left and len(candidate_node_vals) > 1:  # right child w/ no left sibling
                preorder_index = 1
            elif len(candidate_node_vals) > 2:
                preorder_index = 2
            # "fill in" the right child pointer  
            right_subtree_index = -1
            if len(preorder) > preorder_index:
                right_subtree_index = _index(inorder, preorder[preorder_index])
                if right_subtree_index > -1:
                    root.right = _construct_tree(
                        preorder[preorder_index:], 
                        inorder[root_val_index + 1:]
                    )
            return root
        
        ### DRIVER
        # special case: all left children at all
        if preorder and inorder == preorder:
            return _construct_imbalanced(preorder) 
        else:
            return _construct_tree(preorder, inorder) 

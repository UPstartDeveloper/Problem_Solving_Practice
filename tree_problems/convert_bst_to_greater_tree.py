from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        LeetCode: https://leetcode.com/problems/convert-bst-to-greater-tree/
        
        Intuition
            in order DFS
            
        ASSUme we don't need to preserve the search property
            
        Approach:
            linear time and space
            A: 1 DFS --> get sorted values of tree in arr
            B: get a suffix sum arr of the sorted arr
            C: DFS again
                this time - update each node using value 
                at the corresponding ndx in the 2nd array
                
            linear time
            new_value = total_sum - (sum_so_far + original) + original
                
            
            
        
        
        """
        ### HELPERS        
        def _get_total(node, total):
            if node:
                total = _get_total(node.left, total)
                total += node.val
                total = _get_total(node.right, total)
            return total
        
        def _update_nodes(node, total, ssf=0):
            if node:
                ssf = _update_nodes(node.left, total, ssf)
                # "visit"
                original = node.val
                node.val = total - ssf
                ssf += original
                ssf = _update_nodes(node.right, total, ssf)
            return ssf
        
        ### DRIVER
        if root is not None:
            # A: get total sum
            total = _get_total(root, 0)
            # B: update node values
            _update_nodes(root, total)
        # C: return 
        return root
        

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        LeetCode: https://leetcode.com/problems/path-sum/
        
        Input:
            binary tree
            unsorted
            don't know structure, e.g. complete, perfect, full, etc.
            pos/neg
            immutable
            
            + 
            targetSum - pos/neg int
                - can be found adding a root to leaf back
                
        Output:
            bool - presence of R2L sum
            
        Intuition:
            DFS
            backtracking
            
        EC: 
            null root --> return False
            
        Approach:
        
            Subproblem: @node, what is all r2l sums?
                Base: node is a leaf
                    return node.val
                Recursive:
                    n2l_sums = [recurse on each child]
                    return node.val + n2l_sums
                
            At the root --> return if tS in its r2L sums
        
        """
        ### HELPER
        def _check_node_to_leaf_sums(node, sum_so_far):
            if node:
                # visit this node
                sum_so_far += node.val
                if node.left or node.right:
                    # recurse downstream
                    for c in [node.left, node.right]:
                        if c:
                            _check_node_to_leaf_sums(c, sum_so_far)
                else:  # at leaves only
                    # afterward - see if we can have reached the target
                    if sum_so_far == targetSum and not self.is_path_sum:
                        self.is_path_sum = True
            
        ### MAIN
        self.is_path_sum = False
        if root is not None:
            _check_node_to_leaf_sums(root, 0)
        return self.is_path_sum

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_target_copy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        LeetCode: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
        
        Input:
            2 trees + treenode
            cannot assume any structure / not search
            assume:
                node != null
                target node in tree1
                trees are not empty
                node.val - pos/neg, unique
                
        Output:
            node ref
            
        Intuition:
            DFS
            
        Approach:
        
          1) "2 Pass": - O(n) time + space
              1st: find the "pos" of target
              2nd: find the cloned[pos] ==> return node
        
        """
        ### HELPERS
        def _find_pos(original, target):
            '''iterative in-orer DFS'''
            node, stack = original, list()  # top is last index
            visits = 0
            
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    
                    # "Visit"
                    visits += 1
                    if node == target:
                        break
                    
                    node = node.right
                
            return visits
        
        def _find_node(node, target_pos, visits):
            '''recursive in-order DFS'''
            if node:
                visits = _find_node(node.left, target_pos, visits)
                visits += 1
                # check if we've reached the target
                if visits == target_pos:
                    self.corr_node = node
                visits = _find_node(node.right, target_pos, visits)
            return visits
        
        ### DRIVER
        # A: [edge case]
        if (
            not isinstance(original, TreeNode) or 
            not isinstance(cloned, TreeNode) or
            not isinstance(target, TreeNode)
        ):
            raise ValueError("sorry, at least 1 of [original,cloned,target] is not a TreeNode")
        # B: 1st DFS -> locate the node
        node_pos = _find_pos(original, target)
        # C: 2nd DFS -> locate the clone
        self.corr_node = None
        if node_pos > 0:
            _find_node(cloned, node_pos, 0) 
        return self.corr_node

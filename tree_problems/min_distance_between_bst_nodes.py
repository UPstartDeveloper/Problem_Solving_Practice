from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        """
        LeetCode: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
        
        brute force:
            time  / space
            O(n^2) O(n)
            inorder ---> arr
            two nested for loops --> min 
            
            O(n), O(n)
            inorder ---> arr
            two pointers --> min distance (between value)
            
            O(n), O(1)                                                                                                                            
        
        
        """
        ### HELPERS
        def _min_diff_arr(root):
            # 1) DFS - get array
            values = list()
            node, stack = root, list()
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    values.append(node.val)
                    node = node.right

            # 2) find min diff - 2 pointers
            min_diff = float("inf")
            for ndx1 in range(len(values) - 1):
                diff = values[ndx1 + 1] - values[ndx1]
                min_diff = min(diff, min_diff)
            return min_diff
        
        def _min_diff_pointers(node, prev=-1):
            # Base case: node is a leaf
            if node:
                _min_diff_pointers(node.left, prev)
                # visit
                if prev != -1:
                    diff = abs(node.val - prev)
                    self.min_diff = min(diff, self.min_diff)
                prev = node.val
                _min_diff_pointers(node.right, prev)
            return self.min_diff
                
            
        
        ### APPROACH #1: using an array + DFS (linear t/s)
        return _min_diff_arr(root)
        
        ### APPROACH #2: pointers  (linear t, tree needs balance)
        # self.min_diff = float("inf")
        # return _min_diff_pointers(root)
        
        

        

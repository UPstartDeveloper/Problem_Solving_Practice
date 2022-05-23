from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        LeetCode: https://leetcode.com/problems/deepest-leaves-sum
        
        Input:
            binary tree - arbitrary
                not search
                not complete
                not full
            
            pos int values
            
            Assume non-null root
            
        Output: 
            Deepest Leaves sum
                - find the highest depth of any node
                - collect all the nodes at that depth - should be leaves
                - sum their values together
                
        Intuition:
            BFS - when all the nodes in the queue are leaves, sum
            DFS - not sure if it would be as robust
            
        EC:
            1) null root - N/A
            2) not all leaves at same depth 
                - would not be an issue with BFS
            3) val is out of range - ValueError
            4) TODO
            
        Approach:
            
            1) iterative BFS
                "visit" - check if the queue has any non-leaves
                if so - move to next level
                if it does not - sum values in the queue, return
                
                O(n) - n = # nodes
                O(n) - size of queue, worst case
        
        """
        ### HELPERS
        def _dfs(node):
            """iterative, in-order traversal"""
            current_depth, stack, level_leaves = 0, list(), dict()

            # iterative DFS
            while node or stack:
                if node:
                    stack.append((node, current_depth))
                    node = node.left
                    current_depth += 1
                else:
                    node, current_depth = stack.pop()
                    # visit - if it's a leaf, record the depth
                    if node.left is None and node.right is None:
                        # TODO[refactor] - use a defaultdict to cleanup syntax
                        if current_depth in level_leaves:
                            level_leaves[current_depth].append(node.val)
                        else:
                            level_leaves[current_depth] = [node.val]
                    node = node.right
                    current_depth += 1

            return level_leaves

        ### DRIVER
        if not root:
            return 0

        # find all leaves
        level_leaves = _dfs(root)
        # sum the leaves
        deepest = max(level_leaves.keys())
        return sum(level_leaves[deepest])

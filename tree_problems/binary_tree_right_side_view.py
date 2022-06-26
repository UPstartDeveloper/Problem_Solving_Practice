from collections import deque
from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/

        Input:
            tree:
                binary tree, immutable, int, pos/neg
                possibly null
                
        Output:
            List[int]: right side:
                "nodes w/ nothing to thr right"

        Intuition:
            preorder DFS - right chilcdre, BEFORE left
            BFS - last ndoe in each level
            
        EC:
            null tree --> return empty []
            node.val is not an int/out of range --> ValueError
            
        Approach:
            
            1) DFS - O(n + h)
                A: preorder - find depth of tree
                B: init node_vals array - have h zeros 
                C: inorder - populate the array
                    pass the level
                    when visiting - place val at node_vals[level]
                    recurse on left, then the right (so it overwrites as needed)

        """
        ### HELPERS
        def _dfs(node):
            """TODO: debug for trees w/ lots of levels"""
            if node:
                ...

        def _bfs(node):
            """iterative level-order traversal"""
            queue = q = deque([node])
            while queue:
                level_len = len(q)
                for count in range(level_len):
                    node = q.popleft()
                    # visit op
                    if count == level_len - 1:
                        if not isinstance(node.val, int) and -100 <= node.val <= 100:
                            raise ValueError(
                                f"Expect node.val to be int in range [-100, 100], actual is {node.val}."
                            )
                        else:
                            visit(node)
                    # enqueue children
                    for child in [node.left, node.right]:
                        if child:
                            q.append(child)

        ### DRIVER
        self.node_vals = list()

        if root:
            visit = lambda node: self.node_vals.append(node.val)
            _bfs(root)
            # _dfs(root)

        # all done!
        return self.node_vals

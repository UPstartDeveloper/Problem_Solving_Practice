from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        LeetCode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        
        Input:
            binary tree
                no assumption about structure
                could be empty 
                pos/neg values, duplicates
        
        Output:
            2D int array
                every other row is reversed
            
        Intuition:
            BFS
           
        EC:
            empty tree -> return empty []?
            
        Approach:
        
            iterative BFS - visit a level at a time
        
        """
        ### HELPER

        def _bfs(root):
            output = []

            queue = q = deque([root])

            while queue:
                # current level = all nodes in queue
                current_level = [n.val for n in queue]

                # visit(current level) --> adds arr to output
                output.append(current_level)

                # enqueue(next level)
                level_size = len(current_level)
                for _ in range(level_size):
                    node = q.popleft()
                    for child in [node.left, node.right]:
                        if child is not None:
                            q.append(child)

            return output

        ### DRIVERs
        # [check EC]
        if root is None:
            return []

        # BFS
        nodes = _bfs(root)

        # reverse every other level
        for index, row in enumerate(nodes):
            if index % 2 > 0:
                row.reverse()
        return nodes

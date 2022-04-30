# Original Leetcode Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepthBFS(self, root: TreeNode) -> int:
        depth = 0

        if root is not None:
            q = deque([root])

            while q:
                level_length = len(q)

                for _ in range(level_length):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                depth += 1

        return depth

    ########################################################################
    # DFS APProach
    ########################################################################

    class TreeNode:
        """Definition for a binary tree node."""

        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class Solution:
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        """
        Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
        
        Input/Problem:
            - values don't matter
            - includes all the obj
            - any kind of tree
            - include dupes
        
        EC:
            - null root ---> 0
            
        Intuition:
            - path = route between root and leaf
            - max(path lengths) ---> linear search + DFS
        
        Complexity: O(n) time and space

        """
        ### HELPERS
        def _max_depth_search(node, current_depth=1):
            if node is not None:
                # Base: leaf node reached
                if node.left is None and node.right is None:
                    # update self.max_depth
                    self.max_depth = max(self.max_depth, current_depth)
                # Recursive: keep movin' down
                else:
                    _max_depth_search(node.left, current_depth + 1)
                    _max_depth_search(node.right, current_depth + 1)

        ### MAIN
        # A: init max_depth - TODO[refactor if needed]
        self.max_depth = 0
        # B: check edge case
        if root is not None:
            _max_depth_search(root)  # goal: find max_depth
        return self.max_depth

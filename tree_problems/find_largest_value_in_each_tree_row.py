from collections import deque
from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ### HELPERS
        def _bfs_iterative(first) -> List[int]:
            maxes = list()
            queue = q = deque([first])
            while len(q) > 0:
                # dequeue the current level
                level_length = ll = len(q)
                level_max = float("-inf")
                # visit
                for _ in range(ll):
                    node = q.popleft()
                    level_max = max(level_max, node.val)
                    # enqueue next level
                    for child in [node.left, node.right]:
                        if child:
                            q.append(child)
                maxes.append(level_max)
            return maxes

        ### EC
        if not root:
            return []
        ### DRIVER

        # A: run a BFS, where "visit" = max(level) for each level
        max_per_level = mpl = _bfs_iterative(root)
        # B: return the ^output arr
        return mpl

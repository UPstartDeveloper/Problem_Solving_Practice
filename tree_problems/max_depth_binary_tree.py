# Original Leetcode Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
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

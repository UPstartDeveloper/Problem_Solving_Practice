# Original Leetcode problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Brute Force:

        1. BFS (breadth-search search)
            - before: init []
            - during: append queue --> []
            3 --
               q:  [9, 20]
               matrix --> []
            - after: return 2D

            [5, 6, 7, 8]

            let n = # nodes in the tree

            Time: O(n)
            Space: O(2n) --> O(n)


             n / 2 --> 5 / 2

             2 nodes long
             5 nodes

             8 total
             1
             2
             4
             1


        """

        # A: init matrix
        matrix = []  # O(1) time, O(n) space

        # B: validate root
        if root is not None:  # O(1)

            # C: BFS
            q = deque([root])  # O(1), O(n / 2) --> O(n) space

            while len(q):  # num_levels - log(n) --- n iteration

                # add the next level
                matrix.append(
                    [node.val for node in q]
                )  # worst - n/2, best - 1 iteration

                # go on to the next level below
                level_size = len(q)
                for _ in range(level_size):  # worst - n/2, best - 1 iteration
                    node = q.popleft()
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)

        # D: return matrix
        return matrix  # O(1)

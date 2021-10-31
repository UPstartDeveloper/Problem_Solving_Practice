from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Definition for a binary tree node."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Input/Problem:
            - distinct pos ints
            - >= 2 nodes
            - depth - range(0)
            - x != y
            - ASSUME in the tree
            - not search
            - cousins: depth1 == depth2 and parents !=

        EC:
            - unbalanced

        Intuition:
            BFS = calculate depths
            DFS = calculate parents of nodes
            hash map:
                {node_val: parent_val}
                {
                    1: -1,
                    2: 1,
                    3: 1,
                    4: 1
                }
                {depth: [node_val]}
                {
                    0: {1},
                    1: {2, 3},
                    2: {4}
                }

        Approach:
            1) BFS
                # A: BFS ---> dict of depth-nodes
                # B: BFS --> dict node-parents
                # C: check if x and y in same depth
                # D: check if parent_x != parent_y

            2) DFS (recursive) - same time, possibly better space
                A: for both nodes:
                    1) DFS --> find parent
                    2) DFS --> calculate the depth
                B: compare the parents and depths
        """

        ### HELPERS
        def _find_parent(node, target, parent=None):
            """recursive preorder DFS - can be used for approach #2"""
            if node:
                if node.val == target:
                    return parent
                answer_left = _find_parent(node.left, target, node)
                if answer_left:  # it found the parent
                    return answer_left
                answer_right = _find_parent(node.right, target, node)
                if answer_right:  # parent found?
                    return answer_right
            # parent not found
            return None

        def _map_depths_and_parents(root):
            """iterative BFS - front = index 0; back = last index"""
            q = deque([root])
            current_depth = 0
            depths = dict()
            node_parents = {root.val: -1}
            # traverse
            while len(q) > 0:
                # map the current_depth to nodes in the current_level
                level_nodes = set([node.val for node in q])
                depths[current_depth] = level_nodes
                current_depth += 1
                # map children -> parents + update the queue
                for _ in range(len(level_nodes)):
                    parent = q.popleft()  # dequeue
                    for child in [parent.left, parent.right]:
                        if child is not None:
                            node_parents[child.val] = parent.val
                            q.append(child)
            return depths, node_parents

        def _are_depths_same(x, y, depths):
            """iterate through the dict"""
            for nodes in depths.values():
                if x in nodes and y in nodes:
                    return True
            return False

        ### DRIVER
        # A&B: BFS --> dict of depth-nodes and parents of nodes
        depths, node_parents = _map_depths_and_parents(root)
        # C&D: check if cousins
        are_depths_same, are_parents_different = (
            _are_depths_same(x, y, depths),
            (node_parents[x] != node_parents[y]),
        )
        return are_depths_same and are_parents_different


"""
root = 1
x = 4
y = 3
depths = {
    0: {1},   
    1: {2, 3},   
    2: {4}  <-
}

np = {
    1: -1,
    2: 1,
    3: 1,
    4: 2, 
}

is_same_depth = False
"""

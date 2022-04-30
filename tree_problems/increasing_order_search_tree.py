class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """LeetCode: https://leetcode.com/problems/increasing-order-search-tree/"""
        ### HELPERS
        def _traverse(root):
            """iterative, in-order DFS"""
            visited = list()
            node, stack = root, list()  # last index = top of stack
            while node or len(stack) > 0:
                if node:
                    # defer - go down left branch
                    stack.append(node)
                    node = node.left
                else:  # not node
                    node = stack.pop()
                    # visit
                    visited.append(node)
                    # go down the right branch
                    node = node.right
            return visited

        ### DRIVER
        new_root = nr = root
        if root is not None:
            # A: sort nodes
            sorted_nodes = _traverse(root)
            nr = sorted_nodes[0]
            node_index = ni = 0
            # B: rearrange node pointers
            while ni < len(sorted_nodes) - 1:
                node1, node2 = sorted_nodes[ni], sorted_nodes[ni + 1]
                node1.left = None
                node1.right = node2
                ni += 1
            # C: ensure no  cycles
            sorted_nodes[-1].left = None
        return nr

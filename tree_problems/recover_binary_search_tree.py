# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ### HELPER
        def _find_ooo(node, left=list(), right=list()):
            if node:
                left.extend(_find_ooo(node.left))
                right.extend(_find_ooo(node.right))
                # visit: see if the node we have is in order

        ### DRIVER
        if root is not None:
            self.out_of_order = list()
            # A: do a DFS to try "sorting" the nodes in order
            all_nodes = _find_ooo(root)
            # B: locate the output of place nodes - see where prev < node < next is false (watch out for IndexError)
            ...
            # C: EC: if 1 found, check if the root or last leaf is out of place - use _find_ooo
            ...
            # D: swap them back into place
            node1, node2 = self.out_of_order
            node1.val, node2.val = node2.val, node1.val
        return root

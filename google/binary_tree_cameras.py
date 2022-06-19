from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    PLEASE_COVER = 0
    COVERED = 1
    HAS_CAMERA = 2

    def __init__(self):
        self.num_cameras = self.nc = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def _recursive_helper(node):
            '''recursive post order DFS'''
            # null node - doesn't need us to do anything
            if not node:
                return self.COVERED

            # visit the children first
            left_status, right_status = (
                _recursive_helper(node.left),
                _recursive_helper(node.right),
            )

            # if any child not covered --> add camera
            if left_status == self.PLEASE_COVER or right_status == self.PLEASE_COVER:
                self.nc += 1
                return self.HAS_CAMERA

            # if no child covering us - we need to ask our parent to add a camera
            if left_status != self.HAS_CAMERA and right_status != self.HAS_CAMERA:
                return self.PLEASE_COVER

            # otherwise we all good
            else:  # either one of both kids has a camera
                return self.COVERED

        ### GUARD clauses
        if not root:
            return 0

        ### DRIVER
        dummy_node = TreeNode(left=root)
        _ = _recursive_helper(dummy_node)
        return self.nc

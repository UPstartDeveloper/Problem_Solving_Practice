class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """https://leetcode.com/problems/binary-tree-paths/"""

        ### HELPERS
        def _find_paths(node, current_path, all_paths):
            current_path.append(node.val)  # TODO[test]

            # Base:
            if node.left is None and node.right is None:
                # add a full path to all_paths
                all_paths.append([str(val) for val in current_path[:]])

            # Recursive
            else:
                for child in [node.left, node.right]:
                    if child is not None:
                        _find_paths(child, current_path, all_paths)
                        current_path.pop()

            return all_paths

        ### DRIVER
        if root is None:
            return []
        # A: find a list of all paths
        paths = _find_paths(root, list(), list())  # TODO[list of list[int]]
        # C: return all paths - watch the formatting
        return ["->".join(path) for path in paths]

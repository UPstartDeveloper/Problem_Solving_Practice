from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """LeetCode: https://leetcode.com/problems/find-duplicate-subtrees/"""
        ### HELPER(s)
        def _is_duplicates(node1, node2, roots):
            # base cases
            if not node1 and node2:
                return False
            if node2 and not node1:
                return False
            if node1 is None and node2 is None:
                return True

            # recursive case
            elif node1 and node2 and node1 != node2:
                # duplicates found!
                if (
                    node1.val == node2.val and
                    _is_duplicates(node1.left, node2.left, roots) and
                    _is_duplicates(node1.right, node2.right, roots)
                ):
                    # add to the return value
                    if node1.val not in roots:
                        roots[node1.val] = set([node1])
                    else:
                        roots[node1.val].add(node1)
                    return True

                else: # duplicate not found - try the remaining options
                    _is_duplicates(node1, node2.left, roots)
                    _is_duplicates(node1, node2.right, roots)
                    _is_duplicates(node1.right, node2, roots)
                    _is_duplicates(node1.left, node2, roots)
                return False

        ### DRIVERs
        roots = dict()
        if root is not None:
            _is_duplicates(root.left, root.right, roots)
        
        ans = list()
        for node_set in roots.values():
            ans.extend(list(node_set))
        return ans        

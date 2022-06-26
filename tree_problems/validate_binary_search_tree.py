from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        LeetCode: https://leetcode.com/problems/validate-binary-search-tree/
        
        Input:
            binary tree:
                assume root is not null
                32-bit int (pos/neg)
                balanced, unbalanced
        Output: bool
        
        Intution:
            in-order DFS --> sorted. arr
            [1, 5, 3, 4, 6]
                ^  ^        
        EC:
            dupes? --> false
            
        Approach:
        
            1) in-order DFS + array
                [values]
                + linear pass ---> 2 index
                - O(n), O(n)
        """
        ### HELPERS
        def _postorder_recursive(node):
            if node:
                # base case: leaf node
                if not node.left and not node.right:
                    return (node.val, node.val)

                # visit left subtree
                smallest_largest_left = None
                if node.left:
                    smallest_largest_left = _postorder_recursive(node.left)

                # visit right subtree
                if node.right:
                    smallest_largest_right = _postorder_recursive(node.right)
                else:
                    smallest_largest_right = None

                # check this subtree - valid case #1
                if smallest_largest_left and smallest_largest_right:
                    if (
                        smallest_largest_left[1] < node.val
                        and node.val < smallest_largest_right[0]
                    ):
                        return (smallest_largest_left[0], smallest_largest_right[1])
                # valid case #2
                elif smallest_largest_left:
                    if smallest_largest_left[1] < node.val:
                        return (smallest_largest_left[0], node.val)
                # valid case #3
                elif smallest_largest_right:
                    if node.val < smallest_largest_right[0]:
                        return (
                            node.val,
                            smallest_largest_right[1],
                        )
                # invalid case
                self.is_valid = False
                # invalid subtree - make it impossible for others to work
                return (float("inf"), float("-inf"))

        ### DRIVER
        self.is_valid = True
        if root:
            _postorder_recursive(root)  # O(n)
        return self.is_valid

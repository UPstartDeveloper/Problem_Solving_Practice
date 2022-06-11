from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        LeetCode: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

        Input:
            
            root: valid BST, immutable, arbitrary depth
            k: pos/neg (just like node vals)
            
        Output: bool
        
        Intution:
            DFS
            BFS
            two pointers
        
        EC: 
            empty tree - N/A
            invalid input - non-integers, out of range, BST is unordered
            TODO
            
        Approach:
        
            1) Brute Force - O(n^2), O(n)
                search for the complement at each node (BFS/DFS + binary)
                
            2) Array - O(n), O(n)
                DFS on the BST ---> sorted(arr)
                two pters --> O(n)
            
            3) Two Pointers, in the Tree - ???     
        
        """

        ### HELPERs
        def _search(node, value) -> Optional[TreeNode]:
            """recursive binary search on BST"""
            if node:
                if node.val == value:
                    return node
                elif value > node.val:
                    return _search(node.right, value)
                else:  # value < node.val
                    return _search(node.left, value)
            return None

        ### DRIVER

        # BRUTE force - iterative in-order traversal
        node, stack, target = root, list(), k

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                found = _search(root, target - node.val)
                if found and found != node:
                    return True
                node = node.right

        return False

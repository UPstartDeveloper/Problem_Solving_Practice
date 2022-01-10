from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Leetcode: https://leetcode.com/problems/delete-node-in-a-bst
        
        Input/Problem:
            BST - valid mutable, can be empty, pos/neg, unique
            key - int - maybe in the tree
            
        Output: 
            root of modified BST
            
        Intuition:
            1) binary search
            2) deletion: keep ref to parent of node_to_delete
                node has 0 kids ---> get rid of it and done (constant)
                node has 1 kid ---> promote child to take node's 
                node has 2 kids --->
                    TODO: test
                    1) choose the inorder sucessor ---> go right once, then as left as possible
                    2) swap the node_being_deleted w/ successor
                    3) delete the node where the key was moved to 
        
        """
        ### HELPERS
        def _search(root, key):
            parent, node = None, root
            while node is not None and node.val != key:
                parent = node
                if key < node.val:
                    node = node.left
                else:  # key > node.val
                    node = node.right
            return parent, node  # node may be None

        def _find_successor(node):
            """returns a bool (to tell if the node has 2 kids) and the successor"""
            # case 0
            if node.left is None and node.right is None:
                return False, None
            # case 2:
            elif node.left and node.right:
                parent, successor = node, node.right
                while successor.left is not None:
                    parent = successor
                    successor = successor.left
                return True, successor
            # case 1
            elif node.left is not None and node.right is None:
                return False, node.left
            else:  # only 1 child, and it's the right child
                return False, node.right

        def _delete(parent, n2d):
            # double check we have valid inputs
            if n2d is not None and n2d.val == key:
                # choose the inorder successor (3 cases)
                has_two_kids, successor = _find_successor(n2d)
                # make the changes
                if successor is None:  # n2d has 0 kids
                    if parent and n2d == parent.left:
                        parent.left = None
                    elif parent and n2d == parent.right:  # n2d == parent.right
                        parent.right = None
                    return None
                elif has_two_kids:  # node had 2 kids
                    # copy the value of the successor
                    new_value = successor.val
                    # delete the successor
                    self.deleteNode(root, new_value)
                    # update the value of the node to delete
                    n2d.val = new_value
                    return n2d
                elif has_two_kids is False:  # 1 kid
                    if parent and n2d == parent.left:
                        parent.left = successor
                    elif parent and n2d == parent.right:
                        parent.right = successor
                    return successor

        ### DRIVER
        # A: edge cases:
        if root is not None:
            # B: find the node to delete
            parent, n2d = _search(root, key)
            # C: make the deletion - return the node now in the place of the node
            if n2d is not None:  # key is actually in the tree
                takeover_node = _delete(parent, n2d)
                # TODO[test] updating the root node
                if root.val == key:
                    root = takeover_node
        # D: return the root
        return root

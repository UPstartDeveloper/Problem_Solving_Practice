from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left, self.right = left, right\
    

class BSTNode(TreeNode):
    def get_inorder_successor(self) -> List["BSTNode","BSTNode", bool]:
        """Assume the node has a right subtree"""
        pass


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, new: BSTNode) -> None:
        if self.root is None:
            self.root = new
        else:  # first find the leaf
            prev, node = None, self.root
            while node is not None:
                prev = node
                if new.val <= node.val:
                    node = node.left
                elif new.val > node.val:
                    node = node.right
            # put the new node into the tree
            if node == prev.left:
                prev.left = new
            else:  # node == prev.right
                prev.right = new

    def search(self, value: int) -> BSTNode:
        # check is tree is not None
        if self.root is not None:
            node = self.root
            while node is not None and node.val != value:
                if value < node.val:
                    node = node.left
                else:  # value > node.val
                    node = node.right
            return node  # can be null, is value not in the tree
        return None

    def delete(self, value: int) -> BSTNode:
        pass

    def get_all_values(self) -> List[int]:
        """Return a list of all stored ints, in an sorted array."""
        pass
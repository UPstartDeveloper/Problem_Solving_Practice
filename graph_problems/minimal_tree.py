#!/usr/bin/env python3
from typing import List

# Problem: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class MinimalTree:
    def __init__(self, integers: List[int]):
        self.integers = integers
        self.root = None

    def populate_tree(self) -> TreeNode:
        """
        Solution to the problem. Builds the tree and returns the root node.
        """

        def add_subtree(items, parent):
            # Base Case: 2 items left to add
            if len(items) == 2:
                # make nodes for both remaining items
                child, grandchild = (TreeNode(items[1]), TreeNode(items[0]))
                # make the right child the greater element,
                parent.right = child
                # make the smaller element the grandchild of the parent
                child.left = grandchild
            # Recursive Case: > 2 items to add
            elif len(items) == 1 or len(items) > 2:
                # make a new TreeNode
                middle_idx = len(items // 2)
                child = TreeNode(items[middle_idx])
                # add it as either the left or right child of the parent
                if parent.left is None:
                    parent.left = child
                else:  # parent.right is None
                    parent.right = child
                # form the left and right subtrees of this node
                add_subtree(self.integers[:middle_idx], child)
                add_subtree(self.integers[middle_idx + 1 :], child)

        # make the root node of the tree
        middle_idx = len(self.integers // 2)
        self.root = TreeNode(self.integers[middle_idx])
        # make the left subtree from the root
        add_subtree(self.integers[:middle_idx], self.root)
        # make the right subtree from the root
        add_subtree(self.integers[middle_idx + 1 :], self.root)
        # return the root
        return self.root

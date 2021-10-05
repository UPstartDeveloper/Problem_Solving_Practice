"""
Check Balanced: 

Implement a function to check if a binary tree is balanced. 

For the purposes of this question, 

a balanced tree is defined to be a tree such that 
the heights of the two subtrees of any node never differ by more than one.

Clarifying Questions:

What's the input/output?
- Tree with integer values in the nodes
- output is a boolean
- assume the tree does not have the search property
- assume the nodes can have 0, 1, or 2 nodes

True:
            45
        /       \
    7            4

            6
        /       \
        5        7
                /
                5

False:

    6
       \
        7
        /
        5


Brainstorm:

1. Recursive DFS (post-order):

A: at each node
    - if left is not None:
        - validate the left subtree
        - get the height of the left subtree
    - if right is not None:
        - validate the right subtree
        - get the height of the right subtree
    - compare the heights (validate this root)
    - if F --> return F
    - if T --> return T if it's the root, 
                     or else return height of this node (max(left_sub, right_sub))

# we can return False if any of the roots is F, but can't return T until they are
# so we should

"""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def is_balanced(self):
        if self.left is not None:
            # validate the left subtree, and get the height of the left subtree
            left_height, left_balanced = self.left.is_balanced()
        else:  # self.left is None
            left_height, left_balanced = 0, True
        if self.right is not None:
            # validate the left subtree, and get the height of the left subtree
            right_height, right_balanced = self.right.is_balanced()
        else:  # self.right is None
            right_height, right_balanced = 0, True
        # compare the heights (validate this root)
        self_height = 1 + max(left_height, right_height)
        self_balanced = abs(left_height - right_height) <= 1
        # return the height and balance
        return self_height, self_balanced


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def is_balanced(self) -> bool:
        root_height, root_balanced = self.root.is_balanced()
        return root_balanced

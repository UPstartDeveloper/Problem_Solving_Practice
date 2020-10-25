# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def collect_items(node, items):
            '''Performs a pre-order traversal on a binary tree'''
            # visit the node
            if node is None:
                items.append(node)
            else:  # node is not None
                items.append(node.val)
                # traverse the left subtree, if it exists
                collect_items(node.left, items)
                # traverse the right subtree, if it exists
                collect_items(node.right, items)
            
        # collect items from first tree
        tree1 = list()
        collect_items(p, tree1)
        # collect items from second tree
        tree2 = list()
        collect_items(q, tree2)
        # compare 
        return tree1 == tree2
    
"""
tree1
[1, 2, None, None, 3, None, None]

p = TreeNode(1)
node = p, TreeNode(2), TreeNode(2).left = None, TreeNode(2).right = None, TreeNode(3)
"""
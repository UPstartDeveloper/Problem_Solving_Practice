class TreeNode:
    '''definition of a binary tree node'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode, use_recursion=True) -> bool:
        """
        null values matter
        
        in order 
        
        left
        visit
        right
        
        Positive:
        0  1  2  3  4. 5  6
        3, 2, 4, 1, 4, 2, 3
              ^     ^
            [6, 7, 6, 7]
                ^
        Negative example:
        
        None, 2, 3, 1, None, 2, 3
                 ^.     ^
                 
                 
        Intuition: in-order traverse the tree
                   see if we have the same values on either side of the root
                   
        Approach:
        
        # A: get all the values in an array (recursive DFS)
        # B: two pointers move away from the center in the array
        
        Assume:
        - odd number of tree nodes (including NoneTypes)
        
                              > 1  
                               / \
                            > 2 <  2
                             / \  / \
                            3   4 4  3  
                            
        []
        
                                2
                            /       \
                            4       4
                         
        v = [None, 4, None, 2, None, 4, None]
              l,                         r
        
        Big O
        Time: O(n)
        Space:O(n)
        
        
                                1
                               / \
                              2   2
                               \   \
             3    3 

 
                    0   1   2    3    4   5   6    7    8   9   10
        values = [None, 2, None, 3, None, 1, None, 2, None, 3, None ]
                            
        """  
        def compare_nodes(node1, node2):
            """O(n) time, O(log n) space"""
            # Base Case: we've gone beyond the leaf nodes
            if node1 == node2 == None:
                return True
            # Base Case: nodes are not equal
            elif (node1 is None) or (node2 is None) or (node1.val != node2.val):
                return False
            # Recursive Case: nodes are equal
            elif node1.val == node2.val:
                return (
                    compare_nodes(node1.left, node2.right) and
                    compare_nodes(node1.right, node2.left)
                )
        
        is_symmetric = True
        if root is not None and use_recursion is True:
            is_symmetric = compare_nodes(root.left, root.right)
        return is_symmetric
               
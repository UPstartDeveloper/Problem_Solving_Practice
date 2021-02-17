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
        def _compare_nodes_recursive(node1, node2):
            """O(n) time, O(log n) space"""
            # Base Case: we've gone beyond the leaf nodes
            if node1 == node2 == None:
                return True
            # Base Case: nodes are not equal
            elif ((node1 is None) or (node2 is None) or 
                (node1.val != node2.val)):
                return False
            # Recursive Case: nodes are equal
            elif node1.val == node2.val:
                return (
                    _compare_nodes_recursive(node1.left, node2.right) and
                    _compare_nodes_recursive(node1.right, node2.left)
                )

        def _compare_nodes_iterative(root):
            """
            Idea 1:
            use a BFS - see if the queue at every level reads like a palindrome
            - O(n) time, O(log n) space

            Idea 2:
            use a DFS - O(n) time and O(1) space
            Intuition - see if the left and right subtrees mirror each other
            Approach - iteratively traverse the tree using DFS, 
                        fail fast when != happens
                        - get down to the leaves --> True
                        - two unequal nodes --> False
                        - two equal nodes --> move down
                        - one node is null, other is not --> False
            Edge Cases
            - root is null --> already handled
            - different data types --> don't need to worry about in python
        
            """
            # check the root
            is_symmetric = True
            if root is not None:   
                # init collections
                stack = list()
                # push the first pair of nodes to compare
                stack.append((root.left, root.right))
                # traverse the tree
                while len(stack) > 0:
                    # pop a pair
                    node1, node2 = stack.pop()
                    # check for equality
                    if (node1 == node2 == None):
                        continue
                    elif (
                        (node1 is None) or (node2 is None) or 
                        (node1.val != node2.val)):
                        is_symmetric = False
                        break
                    else:  # nodes are equal
                        # push both of the next pairs to check
                        stack.append((node1.left, node2.right))
                        stack.append((node1.right, node2.left))
            # return the answer 
            return is_symmetric     
        
        is_symmetric = True
        if use_recursion is True:
            if root is not None: 
                is_symmetric = _compare_nodes_recursive(root.left, root.right)
            else:  # use the iterative approach
                is_symmetric = _compare_nodes_iterative(root)
        return is_symmetric
               
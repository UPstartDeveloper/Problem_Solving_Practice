# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
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
        def convert_to_array(root):
            def in_order_traverse(node, visit):
                if node.left is not None:
                    in_order_traverse(node.left, visit)
                else:
                    visit(None)
                # visit this node
                visit(node.val)
                if node.right is not None: 
                    in_order_traverse(node.right, visit)
                else:
                    visit(None)
            # init the array
            values = list()
            in_order_traverse(root, values.append)
            return values
        
        def is_valid(array) -> bool:
            # init the two pointers at the middle
            left, right = (len(array) - 1) // 2, (len(array) - 1) // 2
            # "walk away" from the middle
            while left > -1 and right < len(array):  # n / 2
                left_elem = array[left]
                right_elem = array[right]
                # move on to the next step
                if left_elem == right_elem:
                    left -= 1
                    right += 1
                else:
                    return False
            return True
            
        # A: get all the values in an array (recursive DFS)
        values = convert_to_array(root)
        print(values)
        # B: validate the array
        return is_valid(values)

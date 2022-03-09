from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Input/Problem:
            root node -- ASSUME non null
            immutable
            do:
                - count null nodes in the width of level
                - if between left annd right
                
        Output:  
            max(width)
            
        Intuitionn:
            BFS
            
        EC:
            - linked list
            - null root ---> return 0
            - TODO
       
       Approach:
            
            BFS:
            
                init queue = [first_level]
                largest_width = float("-inf")
                
                traverse the tree:
                
                    level = q.dequeue()  # List[TreeNode]
                    
                    # width = _measure_width_of(level) = 2 pter solution
                    update largest_width = max(width, largest_width)
                    
                    q.enqueue([
                        node.left, node.right for node in level
                        if node is not None
                    ])
                    
                return largest_width
        
        LeetCode: https://leetcode.com/problems/maximum-width-of-binary-tree/
        """
        # Credit to Yi-Hsin Chen for this solution!
        # Each index in queue store node and its "index" in the level
        queue = deque([(root, 0)])
        max_length = 1
        while queue:
            # Calculate width of level
            left_most, right_most = queue[0][1], queue[-1][1]
            max_length = max(max_length, right_most - left_most + 1)
            # Append next level's node into new queue
            for _ in range(len(queue)):
                node, index = queue.popleft()
                # If left, right child exist: append it and its index
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))
        return max_length

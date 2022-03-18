import math
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def insert(self, val: int) -> int:
        new = TreeNode(val)
        q = deque()
        if self.root is not None:
            q.append(self.root)
        while q:
            node = q.popleft()
            if node.left is None:
                node.left = new
                return node.val
            elif node.right is None:
                node.right = new
                return node.val
            for child in [node.left, node.right]:
                if child:
                    q.append(child)

    def get_root(self) -> Optional[TreeNode]:
        if self.root:
            return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

"""
Brute Force:

1) Pointer + BFS
    - root pointer
    
    - insert:
        do a top down, left to right iter_BFS
        add new node to the first missing a child (prefer left)
        
2) ASSUME no deletes
    - "cache" 2D array of all the nodes in each levels
    - size of tree
    - insert:
        size ++
        given floor(log_base2(size)) --> level the node needs to go in
        go to the level above --> traverse like in BFS before
    
3) Self-balancing trees?
    - 


"""

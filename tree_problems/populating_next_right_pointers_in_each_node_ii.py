from collections import deque


class Node:
    """Definition for a Node."""

    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """
        LeetCode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
        
        Input: 
            binary tree
                unbalanced?
                complete - not always
                not full always
                
        Output:
            same root
            modify "next" pters in memory
            
        Intuition:
            BFS - use a pter
        
        EC:
            null root - return null
            linked list? - find
            TODO
            
        Approach:
            TODO
        """
        ### HELPER
        def _bfs_helper(root):
            """iterative"""
            # A: init queue
            q = deque([root])
            # B: traverse the queue
            while len(q) > 0:
                # visit: modify the next pointers
                level_length = len(q)
                for node_index in range(level_length - 1):
                    node = q[node_index]
                    node.next = q[node_index + 1]
                # replace with the next level
                for _ in range(level_length):
                    node = q.popleft()
                    for child in [node.left, node.right]:
                        if child:
                            q.append(child)  # TODO[logic-check]
            # C: all done!
            return root

        ### DRIVER
        if isinstance(root, Node) is False:
            return
        return _bfs_helper(root)

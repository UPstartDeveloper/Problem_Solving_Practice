# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    """
    reminders for interviews
        - ask for permission before running the code
        - don't belabor testing
        - check in
        - ask for test cases - if aren't any, make up 1 that is not too big, but still useful for testing
        - DRIVE
        - never get defensive, always aim to collab
        - be willing to say - I don't know, here's what I can say to the best of my knowledge
        - don't say it if you've solved a problem with the same pattern before
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Input(s):
            p and q - roots of 2 different binary tree

        Output:
            bool: is_identical
                vals
                structure

        Constraints
            we CAN'T assume
                - trees are full
                - trees are complete
                - may or may not be weight/height balanced
                - ergo - trees are not perfect
            CAN assume
                val range --> -100, 100 inclusive

        EC:
            both trees empty ---> True

        BCR:
            time: O(n + m) - should only need to traverse each of the trees once
            space: O(n + m) - but depends on traversal method

        Approaches:

            1) DFS
                a) pre-order traversal
                    i. recursive impl
                        subproblem: a single node and it's subtrees - are they identical?

                    def _is_identical(node1, node2):
                        # visit given nodes

                        ## base cases
                        if not node1 and not node2:
                            return True
                        elif ((not node1) and node2) or ((not node2) and node1):
                            return False

                        elif node1.val != node2.val:
                            return False

                        ## recursive case:
                        else:  # node1.val == node2.val:

                            # check left subtrees
                            if node1.left and not node2.left:
                                return False

                            elif node2.left and not node1.left:
                                return False

                            are_lefts_equal = recurse on lefts



                            # check right subtrees
                            # are_rights_equal = ^repeat pattern above

                            return are_lefts_equal and are_rights_equal

        """
        ### HELPER(s)
        def _are_identical_trees_dfs(node1, node2) -> bool:
            """TODO[refactor]: make more DRY"""
            # visit given nodes
            ## base cases
            if not node1 and not node2:
                return True

            elif ((not node1) and node2) or ((not node2) and node1):
                return False

            elif node1.val != node2.val:
                return False

            ## recursive case:
            else:  # node1.val == node2.val:

                # check left subtrees
                if node1.left and not node2.left:
                    return False

                elif node2.left and not node1.left:
                    return False

                # recurse!
                are_lefts_equal = _are_identical_trees(node1.left, node2.left)

                # check right subtrees
                if node1.right and not node2.right:
                    return False

                elif node2.right and not node1.right:
                    return False

                # recurse!
                are_rights_equal = _are_identical_trees(node1.right, node2.right)

                return are_lefts_equal and are_rights_equal

        def _format_tree_bfs(root):
            # plain bfs
            queue = q = deque()
            visited = []

            if root:
                q.append(root)

                while q:
                    current_node = q.popleft()

                    visited.append(current_node)

                    if current_node:
                        q.append(current_node.left)
                        q.append(current_node.right)

            return visited

        ### DRIVER
        # return _are_identical_trees_dfs(p, q)

        tree1 = _format_tree_bfs(p)
        tree2 = _format_tree_bfs(q)

        if len(tree1) != len(tree2):
            return False

        for index in range(len(tree1)):
            node1, node2 = tree1[index], tree2[index]
            # fail fast conditions
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            if node1 and node2 and node1.val != node2.val:
                return False
        return True

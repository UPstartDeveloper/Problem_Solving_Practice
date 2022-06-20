class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

        Input:
            root: root of a binary tree
                int vals (dupes possible)
            assume p != q
                if one is the parent of the other --> return parent
                each node is a child of itself

            lowest --> greatest depth
            
        Output:
            TreeNode: the lca
            note: ALWAYS possible

        EC:
            less than 2 nodes --> return the one node
            no tree --> TODO
            p or q not in Tree --> ???

        Intuition:
            DFS/BFS --> O(n)
            find the intersection of two linked lists 

        Example:

                    3
            5               1
        6       2       0       8
              7    4

        5, 3
        1, 3
           ^


              5, 3
        4, 2, 5, 3

        Approach:
            O(n) time, O(n) space
            1: pre-order DFS to find both nodes
                --> return the whole list of TreeNodes to get there
            
            2: traverse both lists to find "intersection"
        """
        ### HELPERS
        def _dfs_helper(node, target, parents):
            '''
            recursive backtracking
            parents = arrayStack, top is last index
            '''
            if node:
                # base case
                if node == target:
                    parents.append(node)
                    return True
                # visit children
                else:
                    found1 = _dfs_helper(node.left, target, parents)
                    found2 = _dfs_helper(node.right, target, parents)
                    if found1 or found2:
                        parents.append(node)
                        return True
            return False

        def _find_common(ancestors1, ancestors2):
            # find the "start" positions to find intersection
            length1, length2 = len(ancestors1), len(ancestors2)
            index1, index2 = 0, 0
            offset = abs(length1 - length2)

            if length1 < length2:
                index2 += offset
            elif length2 < length1:
                index1 += offset

            # find intersection (the first is the lowest)
            while (
                index1 < length1 and 
                index2 < length2 and
                ancestors1[index1] != ancestors2[index2]
            ):
                index1 += 1
                index2 += 1

            # all done!
            return ancestors1[index1]

        ### EC
        if not root:
            raise ValueError("There is no tree")
        
        if not root.left and not root.right:
            return root

        ### DRIVER
        # 1: see above
        node1_ancestors = list()
        _dfs_helper(root, p, node1_ancestors)

        node2_ancestors = list()
        _dfs_helper(root, q, node2_ancestors)

        # 2: see above
        lca = _find_common(node1_ancestors, node2_ancestors)

        return lca

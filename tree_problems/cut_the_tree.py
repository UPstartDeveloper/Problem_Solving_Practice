"""
=====================================================================
Source: https://www.hackerrank.com/challenges/cut-the-tree/problem
=====================================================================

"Cut the Tree" Coding Challenge
tree is UNWEIGHTED

vertices numbered 1 - n
each w/ a data

tree.sum() --> sum of nodes' data values

diff of two trees --> abs(diff of their sums)

INPUT:
data = [ints --> data values of nodes 1 -n]
edges = [(parent, child) tree edges]


OUTPUT:
min possible diff of two trees (can only cut one vertex in input)

Clarifications:

1) is 1 always root? YES
2) undirected - so children know their parents? YES
3) ASSUME our trees are binary (for simplicity's, obv not required)
3) we have at least 3 nodes, pos data values


Intutition:
    - DFS --> compute sum of a tree
    - diff - function
        - DECREASES as the tree sums become more balanced
        - INCREASES as they become further apart 
        - in a balanced tree --> diff increases as we go up the tree

Approach:

1. Brute force 
    - build two trees multiple ways, each time leave out a different edge
        - calc the sum of both in each variation (via BFS, get sum of each set of connected comp)
        - calc the diff in each varation
    - return min diff

2. BFS, then DFS
    - build the entire tree once - each has an id
    - potentially optimize via bottom-up dp - pre-compute the tree sums of every subtree, starting from leaves
    - init a smallest_diff
    - "try every combination" again via BFS
        - calc tree sums --> (parent.val + child_1.sum) vs. (child_2.sum)
        - calc diff
        - update the smallest_diff as necessary

Edge Cases
    - M-way tree, or a graph ---> can just switch over to using an adj. list for representation
    - zero edges --> throw ValueError
    - non pos data value --> ValueError
    - when the largest id nodes aren't leaves - have to be robust against weird tree configs
"""
from collections import deque
from typing import List, Tuple


class TreeNode:
    '''TODO: generalize this to M-Way tree'''
    def __init__(self, id, val):
        self.id = id
        self.val = val
        self.left = self.right = self.parent = None

    def calculate_sum(self):
        """
        the sum of this node plus all the nodes in its subtrees
        """
        total = 0
        stack = list()
        node = self

        # DFS to find total
        while len(stack) > 0 or node is not None:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                total += node.val
                node = node.right

        return total

    def get_parent(self):
        '''get the highest possible parent of this node'''
        parent, node = self.parent, self

        while parent is not None:
            node = parent
            parent = parent.parent

        return node

    def __str__(self):
        return str(self.id)


class Tree:
    def __init__(self, data: List[int], edges: List[Tuple[int]]):
        # A: store list of tree nodes - O(n)
        self.nodes = list()
        for id_val in range(1, len(data) + 1):  # n iterations
            node = TreeNode(id_val, data[id_val - 1])
            self.nodes.append(node)
        # B: connect tree nodes - O(n)
        for edge in edges:
            id1, id2 = edge
            node1, node2 = self.nodes[id1 - 1], self.nodes[id2 - 1]
            if node1.left is None:
                node1.left = node2
            else:
                node1.right = node2
            node2.parent = node1
        # C: set the tree root
        self.root = self.nodes[0]


class Solution:
    """
    COMPLEXITY ANALYSIS
    v = # of nodes
    e = # of edges (in the Hacker Rank challenge, this is assumed to be n - 1)
    tree is NOT guaranteed to be complete or full - i.e. may not always be balanced
    tree is ASSUMED to be binary

    Time: O(n^2), 
    thing to optimize is repeated work is calculating the tree sums

    Space: O(n)
    n + e objects for Tree nodes
    n - largest possible space the stack in a DFS can take up

    """
    def cut_the_tree(self, data: List[int], edges: List[Tuple[int]]):

        # A: build the entire tree once - each has an id - O(n)
        tree = Tree(data, edges)  # 
        # B: find the smallest difference by iterating over the list of edges
        smallest_diff = float("inf")
        for node_id, child_id in edges:  # e iterations ---> overall O(n^2)
            # get the nodes
            node = tree.nodes[node_id - 1]
            child = tree.nodes[child_id - 1]
            # calc diff
            parent = node.get_parent()  # worst case - O(n); best case - O(log n)
            sum1 = child.calculate_sum()  # worst case - O(n)
            sum2 = parent.calculate_sum() - sum1  # worst case - O(n)
            diff = abs(sum1 - sum2)
            # update smallest as appropiate
            if diff < smallest_diff:
                smallest_diff = diff 
        # return solution
        return smallest_diff


if __name__ == "__main__":
        # Test Case from Hacker Rank
        data = [1, 2, 3, 4, 5, 6]
        edges = [
            (1, 2), (1, 3), (2, 6), 
            (3, 4), (3, 5)
        ]
        sol = Solution()
        print(sol.cut_the_tree(data, edges))

"""
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
        TODO: TEST this code
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

    def __str__(self):
        return str(self.id)


class Tree:
    def __init__(self, data: List[int], edges: List[Tuple[int]]):
        # A: store list of tree nodes
        self.nodes = list()
        for id_val in range(1, len(data) + 1):
            node = TreeNode(id_val, data[id_val - 1])
            self.nodes.append(node)
        # B: connect tree nodes
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

    def get_tree_sums(self) -> list:
        # A: init list to hold sums
        sums = [0 for _ in range(len(self.nodes))]
        # B: get the sum of each node, bottom up
        NUM_NODES = len(self.nodes)
        for current_id in range(NUM_NODES, 0, -1):
            node_sum = self.nodes[current_id - 1].calculate_sum()
            sums[current_id - 1] = node_sum
        # C: return the sums
        return sums


class Solution:
    def cut_the_tree(self, data: List[int], edges: List[Tuple[int]]):

        def update_diff(node, smallest_diff, tree_sums):
            # COMBO one
            # - calc tree sums --> (parent.val + child_1.sum) vs. (child_2.sum)
            sum1 = node.val
            if node.left is not None:
                sum1 += tree_sums[node.left.id - 1]
            sum2 = 0
            if node.right is not None:
                sum2 += tree_sums[node.right.id - 1]
            # - calc diff
            diff = abs(sum1 - sum2)
            # - update the smallest_diff as necessary
            if diff < smallest_diff:
                smallest_diff = diff
                print(f"diff: {diff}, node: {node}, sums: {sum1, sum2}")
            # COMBO TWO
            # - calc tree sums --> (parent.val + child_1.sum) vs. (child_2.sum)
            sum1 = node.val
            if node.right is not None:
                sum1 += tree_sums[node.right.id - 1]
            sum2 = 0
            if node.left is not None:
                sum2 += tree_sums[node.left.id - 1]
            # - calc diff
            diff = abs(sum1 - sum2)
            # - update the smallest_diff as necessary
            if diff < smallest_diff:
                smallest_diff = diff
                print(f"diff: {diff}, node: {node}, sums: {sum1, sum2}")
            return smallest_diff

        # A: build the entire tree once - each has an id
        tree = Tree(data, edges)
        # B: potentially optimize via memoization - pre-compute the tree sums of every subtree, starting from leaves
        tree_sums = tree.get_tree_sums()
        # C: init a smallest_diff
        smallest_diff = float("inf")
        # D: "try every combination" again via BFS
        q = deque([tree.root])
        while len(q) > 0:
            # dequeued a node
            node = q.popleft()
            # change the diff --- TODO: refactor
            smallest_diff = update_diff(node, smallest_diff, tree_sums)
            # enqueue neighbors
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
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

"""
Check Subtree: 

T1 and T2 are two very large binary trees, 
with T1 much bigger than T2. 

Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Example:

                    T1

                    6
                 /     \
                3        7   T2
                \      /    \
                 1    6      -7
                /      \
               -5       5

q = [1, 6, -7]
subtree_n = 6               T2_n            equal?
            3                   7              F
            7                   7
            6                   6
           -7                   -7              T

            
Clarification:
1. tree is nothing special? yes
    - not search
    - not balanced (not complete)
    - not full
    - not perfect
2. could there be duplicate values? yes
3. comparing node object addresses or based on values? addresses
4. return boolean
5. can T2 occur anywhere in the tree?


Intuition:
- DFS of a subtree in T1 can == DFS of T2

Approach:
1. Brute Force:
    - iterate through every node in the tree after 1st level (via iterBFS)
        - does an iterDFS of the tree below that node (including it), 
        - simulatenously fail fast while doing the same DFS on T2, to see if equal
        - if whole thing is true, return true right away
    - if no subtree matches, return False overall

    - Problems w/ approach:
    - slow
    - won't handle cases where T2 doesn't include leaves
        - ASSUME not going to happen tho, based on the def above
    - even if we decide to use a BFS to check the subtrees, we'll end up including extra nodes 

Edge Cases:
- one of the trees is null --> False
- if both null ---> False
- T1 == T2 --> False, b/c needs to be a "sub"-tree
- T2 > T1 --->  False, need to check for nulls while doing a DFS
"""
from collections import deque


class BinaryNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def dfs(self) -> list:
        """
        Better way to implement an iterative DFS:
        https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
        """
        # init visited array
        visited = set()
        # init stack
        stack = [self]
        # DFS in-order, fill the visited array
        while stack:
            node = stack[-1]
            while node.left and node.left not in visited:
                stack.append(node.left)
                node = node.left
            top = stack.pop()
            visited.add(top)
            if top.right and top.right not in visited:
                stack.append(top.right)
        # return the array
        return visited


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


class Solution:
    def are_trees_identical(self, root1: BinaryNode, root2: BinaryNode) -> bool:
        # Validate the nodes
        is_equal = False
        if root1 is not None and root2 is not None:
            # DFS (in-order) the subtrees that the nodes are part of
            subtree1_values, T2_values = (root1.dfs(), root2.dfs())
            # compare visited values
            is_equal = subtree1_values == T2_values
        return is_equal

    def check_subtrees(self, t1: BinaryTree, t2: BinaryTree) -> bool:
        # A: validate inputs
        is_found = False

        if t1 is not None and t2 is not None:
            # B: init q to do BFS
            q = deque()
            # C: enq children of T1 root
            if t1.root is not None and t1.root.left is not None:
                q.append(t1.root.left)
            if t1.root is not None and t1.root.right is not None:
                q.append(t1.root.right)
            # D: traverse
            while len(q) > 0:
                # E: dequeue a node
                node = q.popleft()
                # F: if subtree == t2, return True
                if self.are_trees_identical(node, t2.root) is True:
                    is_found = True
                    break
                # G: otherwise enqueue children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return is_found


"""
                    T1

                    6
                 /     \
                3        7   T2
                \      /    \
                 1    6      -7
                /      \
               -5       5

i_f     q           n       r1      r2      i_e
F       [7]         3       3       7        F

v = [3,-5]
stack = [1,]
t = -5
n = -5
"""


if __name__ == "__main__":
    t1 = BinaryTree()
    t1.root = BinaryNode(6)
    t1.root.left = BinaryNode(3)
    t1.root.left.right = BinaryNode(1)
    t1.root.left.right.left = BinaryNode(-5)
    t1.root.right = BinaryNode(7)
    t1.root.right.left = BinaryNode(6)
    t1.root.right.left.right = BinaryNode(5)
    t1.root.right.right = BinaryNode(-7)
    t2 = BinaryTree()
    t2.root = t1.root.right
    sol = Solution()
    print(sol.check_subtrees(t1, t2))

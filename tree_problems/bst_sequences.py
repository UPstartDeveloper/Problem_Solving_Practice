"""
BST Sequences: 

A binary search tree was created by traversing through an array from 
left to right and inserting each element. 

Given a binary search tree with distinct elements, 
print all possible arrays that could have led to this tree.

EXAMPLES

input:
    2 
/       \
1         3

output:
[
    [2, 1, 3], [2, 3, 1]
]

            2 
        /       \
        1         3
      /  \
    -1     1.5

output:
[
    [2, 3, 1, -1, -1.5], --> going to right subtree, the left subtree (left thn right)
    [2, 3, 1, 1.5, -1], --> going to right subtree, the left subtree (right then left)
    [2, 1, 3, -1, 1.5], ---> BFS order
    [2, 1, 3, 1.5, -1], ---> BFS order2
    [2, 1, -1,  3, 1.5], ---> adding the right subtree in the middle of adding the left
    [2, 1, 1.5, 3, -1], ---> 
    [2, 1, -1, 1.5, 3], ---> left dominant
    [2, 1, 1.5, -1, 3], 
]


Clarifications:
1. array of ints? always
2. ASSUME all array elements unique
3. ASSUME: 2D array, input is tree object
4. only one answer, or can arrays be in any order? any order
5. ASSUME that the tree won't always be perfect, like in the example

Intuition:
    - get all the perms of an input int arr --> BST
    - all the nodes of a level, have to be before all nodes of another level
    - # of permutations = # permutations for l - number of nodes in the 
Approach:
    - example output - found through just doing a pre-order traversal, and another thing

    1. Backtracking
    # A: BFS the tree, create 2D array of all nodes in each level
    [
        [2],
        [1, 3]
    ]
    # B: backtrack and create all the permutations:
        - init a list to hold all_perms = []
        - create the combinations
            - create a single permutation
            - has spaces for all n nodes
            - one each stack of the recursion tree, we add another available node into the perm
            - can only choose a node from whatever level we're on
            - if full - add it to the all_perms
            - backtrack to fulfill next perm
             nodes = [ [2], [1, 3], ], level = None, one_perm = [ _,  _,  _]
                        |
        nodes = [[], [1, 3]], level = 0, one_perm = [2, _, _], 
                    /                                       \
nodes = [[], [, 3]], level = 1, one_perm = [2, 1, _],  nodes = [[], [1, ]], level = 1, one_perm = [2, 3, _],
            /                                                   \
nodes = [[], [, ]], level = 1, one_perm = [2, 1, 3],        nodes = [[], [, ]], level = 1, one_perm = [2, 3, 1],    

2. Another BackTracking Approach:
    1. Add the root node first (as always)
    2. then we iterate through adding the left subtree,
        - and also choose different positions for where to start adding the right subtree
"""
from collections import deque
from typing import List


class BinaryTreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left, self.right = None, None


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def to_arrays(self) -> List[List[int]]:
        '''represent nodes in BFS order using arrays'''
        # init output
        nodes = list()
        # init queues
        current_level = deque()
        # enqueue first node
        if self.root is not None:
            current_level.append(self.root)
        # traverse the tree
        while current_level:
            # for each node in this level
            level_values = [node.key for node in current_level]
            # add it to output
            nodes.append(level_values)
            # put their children in next_level q
            level_size = len(current_level)
            for _ in range(level_size):
                node = current_level.popleft()
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
        return nodes

class Solution:
    def compute_permutations(self, nodes: List[List[int]]) -> List[List[int]]:

        def add_all_nodes(current_perm, level_nodes, starting_pos):
            """TODO:
               adds all the nodes from starting index in level_nodes -> current_perm
               accounts for IndexErrors
            """
            index = starting_pos
            for _ in range(len(level_nodes)):
                # find the right value for the index
                if index == len(level_nodes):
                    index = 0
                # add the next node to the perm
                current_perm.append(level_nodes[index])
                # move on to the next value
                index += 1

        def form_perms(all_perms, current_perm, level):
            """
            TODO:
            this method runs, however it leaves out some of the permutations,
            - this is because all nodes in a level appear any nodes of the next level
                - this is too specific - it regards only the permutations in which the 
                 the BST stays balanced throughout
            - really it should be the parent node appears before any of their children
            - variations in how the children appear can be:
               1 - left, left subtree, right
               2 - left, right, left subtree
               3 - right, left, right subtree
               4 - right, right subtree, left
            - currently we only do the #2 and #3
            - the solution also needs to AVOID duplicates, since we are using an array
                to store all eventual permutations
            """
            # A: for any level - grab the level
            level_nodes = nodes[level]
            # B: choose a starting index
            initial_perm = [val for val in current_perm]
            for starting_index in range(len(level_nodes)):
                # C: put all the nodes in this level in the perm, going from starting index
                add_all_nodes(current_perm, level_nodes, starting_index)
                # D: if a next level - 
                if level + 1 < len(nodes):
                    # E: go to the next level
                    form_perms(all_perms, current_perm, level + 1)
                # F: if no next level - add the perm to all_perms
                else:
                    all_perms.append(current_perm)
                # G: when come back, remove all previously added nodes
                current_perm = [val for val in initial_perm]
        
        # A: init a list for all permutations
        all_perms = list()
        # B: go about making the permutations
        form_perms(all_perms, current_perm=list(), level=0)
        # C: return the permutations
        return list(all_perms)

    def bst_sequences(self, tree: BinaryTree):
        # A: make 2D array of tree node keys
        nodes = tree.to_arrays()
        # B: return permuations
        return self.compute_permutations(nodes)


if __name__ == "__main__":
    # Model the test tree in the comments at the top of script
    root = BinaryTreeNode(2)
    tree = BinaryTree(root)
    tree.root.left = BinaryTreeNode(1)
    tree.root.right = BinaryTreeNode(3)
    tree.root.left.left = BinaryTreeNode(-1)
    tree.root.left.right = BinaryTreeNode(1.5)
    # test the solution
    sol = Solution()
    print(sol.bst_sequences(tree))

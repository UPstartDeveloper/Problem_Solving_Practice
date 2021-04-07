"""
Paths with Sum: 
You are given a binary tree in which each node contains an integer value 
(which might be positive or negative). 

Design an algorithm to count 
the number of paths that sum to a given value. 

The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).

Clarifying Questions:
1. is zero allowed? no
2. not a search tree? no
3. do we know anything about the tree structure:
    - balanced? no
    - full? no
    - duplicates allowed? yes
4. does the path strictly go downwards? yes
5. does a path need more than 1 node? no

Example:
   ssf = 14                 6,          value = 14 ---> 1
   c = 1                /      \        value = 0 ---> 1
                      -5         8      
                              /     \   
                             5       4
                            /
                          -5

Intuition:
- searching through all the paths (in all subtrees) to find paths
- enumerate THOSE paths
Approach:
1. Brute Force:
    # - init a count
    # - traverse through all the different paths 
    #     - find a starting node using a BFS
    #         - DFS through all paths that start at that node
    #         - keep track of sum_so_far (ssf)
    #             - anytime we go up - remove the last added values
    #             - down - add to ssf
    #             - if ssf == value---> count +=1, go back up the tree, we're done w/ that subtree
    #             - if we hit a leaf, we're done w/ that branch, go back up
    #             - if we're done w/ all branches, go back up
    # - return the count
Edge Cases:
1. given value is 0? --> return 0 right away
2. null tree --> return 0

"""

from collections import deque


class BinaryNode:
    def __init__(self, key=None):
        self.value= key
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root


class Solution:
    def traverse_from_start(node: BinaryNode, target: int) -> int:
        """
        # - anytime we go up - remove the last added values

        # down - add to ssf
        # if ssf == value---> count +=1, go back up the tree, we're done w/ that subtree
        # if we hit a leaf, we're done w/ that branch, go back up
        # if we're done w/ all branches, go back up
        """
        # keep track of sum_so_far (ssf), init num of paths
        paths_found = 0
        ssf = 0
        stack = list()

        current_node = node

        # DFS
        while stack or current_node:
            if current_node:  # in in-order traversal, we go left
                stack.append(current_node)
                ssf += current_node.value
                current_node = current_node.left
            else:  # gone all the way down the left
                current_node = stack.pop()
                # visit - increment the sum_so_far
                ssf += current_node.value
                # see if we can increment the paths
                if ssf == target:
                    paths_found += 1
                # go back up
                if current_node.left == current_node.right:
                    ssf += (-1 * current_node.value)
                # then, go down the right branch
                if current_node.right:
                    stack.append(current_node.right)

        return paths_found

    def paths_with_sum(self, tree: BinaryTree, target: int) -> int:
        # - init a count
        count = 0
        # validate 
        if (tree is not None and tree.root is not None and target != 0):
            # - traverse through all the different paths via BFS
            q =  deque([tree.root])
            while len(q) > 0:
                # get the node at front of the queue
                node = q.popleft()
                # "visit" DFS through all paths that start at that node
                count += self.traverse_from_start(node, target)
                # enqueue the next nodes to use as a starting nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        # - return the count
        return count

"""
Random Node: You are implementing a binary tree class from scratch which, in addition to 

- insert, 
- find, and 
- delete, 

has a method getRandomNode() 
which returns a random node from the tree. 

All nodes should be equally likely to be chosen. 

Design and implement an algorithm for getRandomNode, 
and explain how you would implement the rest of the methods.

Clarifications
1. Do we know anything else about the kind of tree we need?
    - search? yes - for purpose of knowing how to insert
    - complete/full/perfect? no
2. Size constraints? none
3. Are the keys in the tree unique? no
4. Can it store any data type? ASSUME only integers
5. ASSUME we can use random module in Python

Example:

                3
            /       \
            7       3
          /   \
        1      -4

        [1, 7, -4, 3, 3]

Intuition:
- "throw a dart" and return whatever node it lands on

Approach:
1. Use external array
- do a DFS to get all the nodes in an array
- generate a number between [0, n - 1] 
- return the node in that index in the array

2. Use a property
- keep a .size property for the size of the tree
- in getRandomNode - generate the num r = in range [0, self.size - 1]
- return the rth node we hit when doing a DFS

Edge Case 
1. null tree? - return None

"""
import random


class RandomTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class RandomTree:
    def __init__(self, root: RandomTreeNode):
        self.root = root
        self.size = 1

    def insert(self, node: RandomTreeNode):
        # TODO: increment self.size
        pass

    def find(self, node_val) -> RandomTreeNode:
        pass

    def delete(self, node_val) -> RandomTreeNode:
        # TODO: decrement self.size if node is found
        # otherwise raise ValueError?
        # modify the tree
        pass


    def get_random_node(self) -> RandomTreeNode:
        def _get_rth_node(node_num):
            """returns the node we hit after doing iterative 
            in order DFS for node_num steps
            """
            # A: init collections 
            stack = list()
            # B: push the first node onto stack
            stack.append(self.root)
            # C: count visits taken so far
            visits = 0
            # D: traverse 
            while len(stack) > 0:
                # get the node from the stack top
                node = stack[-1]
                # while it has a left child, push it
                while node.left is not None:
                    stack.append(node.left)
                    node = node.left
                # visit the top at this moment
                top = stack.pop()
                visits += 1
                # if it's the rth node, return it
                if visits == node_num:
                    return top
                # if it has a right child, push it too
                if top.right is not None:
                    stack.append(top.right)

        # A: validate the tree
        if self.size <= 0 or self.root is None:
            raise ValueError("Cannot return node from empty tree.")
        # B: generate the random number
        node_num = random.randrange(1, self.size - 1)
        # C: get the random node
        return _get_rth_node(node_num)

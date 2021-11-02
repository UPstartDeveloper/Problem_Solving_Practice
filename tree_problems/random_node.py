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
3. Are the keys in the tree unique? no, place duplicate values to right
4. Can it store any data type? ASSUME only integers
5. ASSUME we can use random module in Python

Example:

                5
            /       \
            3        7
          /   \
        1      4
      /  \
     -4   2

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

3. HashTable?
    A: on insert --> add the new binary node

Edge Case 
1. null tree? - return None

"""
from collections import deque
import random


class RandomTreeNode1:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class RandomTree1:
    def __init__(self, root=None):
        self.root = root  # ideally a RandomTreenode obj
        self.size = 0
        if self.root is not None:
            self.size = 1

    def insert(self, node_val: int) -> None:
        # A: validate the input
        if isinstance(node_val, int) is False:
            raise ValueError("Could not insert non-integer object")
        # B: binary search for the right position to place the node
        parent, node = None, self.root
        if node is None:  # special case
            self.root = RandomTreeNode1(node_val)
        else:  # +1 levels in the tree
            while node is not None:  # go
                parent = node
                # go left
                if node_val < node.key:
                    node = node.left
                # go right
                else:  # node_val >= node.key
                    node = node.right
            # update the node object to be the new node
            if parent.key > node_val:
                parent.left = RandomTreeNode1(node_val)
            else:  # parent.key <= node_val
                parent.right = RandomTreeNode1(node_val)
        # C: increment self.size
        self.size += 1

    def _find_node(self, node_val):
        # init the parent and node with the value
        parent, node = None, self.root
        # binary search for the node_value in the tree
        while node is not None and node.key != node_val:
            # move the parent pointer
            parent = node
            # go right
            if node.key < node_val:
                node = node.right
            # go left
            elif node.key > node_val:
                node = node.left
        # if node not found, raise error
        if node is None:
            raise ValueError("Node could not be found in this tree.")
        # return what was found
        return parent, node

    def find(self, node_val) -> RandomTreeNode1:
        """
        Finds the first node w/ a key == the given node_val.
        If not found, raises ValueError.
        """
        # A: Validate the tree
        if self.root is None:
            raise RuntimeError("This tree is empty. Cannot be searched.")
        # B: find the node and its parent
        parent, node = self._find_node(node_val)
        # C: return the node, if found
        return node

    def delete(self, node_val) -> RandomTreeNode1:
        """
        Intuition
            - we know the left subtree needs to take the place of its parent
            - we know the right subtree needs to go in the right subtree of the left
        Approach:
            # A: get the parent of the node, and the node
            #     - if not found raise a ValueError
            # B: promote the root of the left subtree to take the deleted nodes place
            #     - - what if it's the root?
            #         - then parent will be None
            #         - so promote via setting self.root attr
            # C: insert the right subtree into the left subtree
            # D: decrement self.size if node is found

        """
        # A: validate the tree
        if self.size <= 0 or self.root is None:
            raise ValueError("Cannot delete node from empty tree.")
        # B: get the parent of the node, and the node
        parent, node = self._find_node(node_val)
        # C: promote the root of the left subtree to take the deleted nodes place
        if node.left is not None:
            # if the deleted node is the root
            if parent is None:
                node.left = self.root
            else:  # parent is not None
                if parent.left == node:
                    parent.left = node.left
                else:  # parent.right == node
                    parent.right = node.left
        # D: re-insert the right subtree into the left subtree
        if node.right is not None:
            self.insert(node.right)
        # E: decrement self.size if node is found
        self.size -= 1
        # F: return the deleted node
        return node

    def get_random_node(self) -> RandomTreeNode1:
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


class RandomNode2:
    def __init__(self, val):
        self.val = val
        self.id = None
        self.left, self.right = None, None


class RandomTree2:
    def __init__(self, root):
        self.node_ids = dict()  # id --> List[RandomNode2]
        if root is not None:
            self.root = root
            self._hash_node(root)

    def _hash_node(self, node):
        hash_id = hash(node)
        node.id = hash_id
        if hash_id not in self.node_ids:
            self.node_ids[hash_id] = set([node])
        else:
            self.node_ids[hash_id].add(node)

    def insert(self, val) -> None:
        ### HELPER
        def _place_node(new_node: RandomNode2) -> None:
            """Add the node as a new leaf, arbritarily move left/right"""
            if self.root is None:
                self.root = new_node
            else:  # move the node down to find a space
                CHOICES = [0, 1]  # 0 = left, 1 = right
                parent, node = None, self.root
                while node is not None:
                    parent = node
                    direction = random.choice(CHOICES)
                    if direction == 0:  # move left
                        node = node.left
                    else:  # move right
                        node = node.right
                # insert the new node
                if parent.left == node:
                    parent.left = new_node
                else:  # new right child
                    parent.right = new_node

        ### DRIVER
        # A: place the node in the tree, structurally
        node = RandomNode2(val)
        _place_node(node)
        # B: insert the node in the hash table
        self._hash_node(node)

    def delete(self, val) -> RandomNode2:
        ### HELPERS
        def _remove_structurally(parent, node):
            # rming the root -> no more action needed
            if parent is not None:
                is_left_child = True
                if parent.right == node:
                    is_left_child = False
                # 0 kids: rm childless node
                if node.left is None and node.right is None:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # 1 kid:
                elif node.left and not node.right:
                    if is_left_child:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                elif node.right and not node.left:
                    if is_left_child:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                # 2 kids:
                else:
                    # choose a subtree a grandchild randomly
                    grandchild = random.choice([node.left, node.right])
                    # promote the grandchild
                    if is_left_child:
                        parent.left = grandchild
                    else:
                        parent.right = grandchild
                    # re-insert the other
                    if node.left is not grandchild:
                        self.insert(node.left)
                    else:
                        self.insert(node.right)

        def _remove_from_dict(node):
            if node.id in self.node_ids:
                nodes = self.node_ids[node.id]
                for n in nodes:
                    if node == n:
                        self.node_ids[node.id].remove(node)

        ### DRIVER
        # find the first node w/ the val
        parent, node = self._find_node(val)
        # rm it from the tree, structurally and from the dict
        _remove_structurally(parent, node)
        _remove_from_dict(node)

    def _find_node(self, val):
        q = deque([(None, self.root)])
        while q:
            parent, node = q.popleft()
            if node.val == val:
                return parent, node
            for child in [node.left, node.right]:
                if child:
                    q.append((parent, child))

    def find(self, val) -> RandomNode2:
        """return the first node w/ the given value via BFS"""
        # tree is there
        if self.root is not None:
            parent, node = self._find_node(val)
            return node
        return None

    def get_random_node(self) -> RandomNode2:
        # choose an id randomly
        hash_id = random.choice(self.node_ids.keys())
        node = random.choice(self.node_ids[hash_id])
        # return the corresponding node
        return node


if __name__ == "__main__":
    tree = RandomTree1()
    tree.insert(5)
    tree.insert(7)
    tree.insert(6)
    assert tree.root.key == 5
    assert tree.root.right.key == 7
    assert tree.root.right.left.key == 6
    assert tree.size == 3

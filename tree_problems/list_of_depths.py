"""
Cracking the Coding Interview 4.3

List of Depths: 

Given a binary tree, design an algorithm which creates a linked list 
of all the nodes at each depth 

(e.g., if you have a tree with depth 0, you'll have 0 linked lists).

Clarifying Questions:

What is the input format? do we have a Tree class?

What do we want to return here? 
- an array of head nodes for each linked list

What do we know about the binary tree?
not much - not a search tree, not complete/full/perfect

- " if you have a tree with depth 0, you'll have 0 linked lists" - so this refers to when 
    we have no nodes in the tree only, yes? yes

Assumptions:

is it ok to use external space? yes
is it ok to use the deque class? yes
data in the nodes are integers

Brainstorm:
Test Input:

                            4
                         /     \
                        2       5
                      /  \        \
                     1    3        7

1: BFS traversal

two arrays 
queue = [1,3, 7] --> iterate over each item here, to get the neighbors
           --> then, do a second pass to make a LL, dequeue the nodes in the queue
           --> then replace the nodes in the queue, with the nodes in the next level
neighbors = [ ]
lists = [4->  , 2->7->    ,     ,   ]

A: enqueue the root node
B: go until there are no more items in the queue and next neighbors
    # 1st pass: enqueue the neighbors of that node (aka item)
    # 2nd pass: make a LL from the nodes in the queue, add 
    # enqueue the neighbors of that node (aka item)
C: return the lists of list nodes

"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, items):
        self.head = ListNode(items[0])
        node = self.head
        for index in range(1, len(items)):
            next_node = List(items[index])
            node.next = next_node
            node = next_node


def list_of_depths(tree: Tree) -> List[LinkedList]:
    q, next_level, lists = deque(), deque(), list()
    # A: enqueue the root node
    q.append(tree.root)
    # B: go until there are no more items in the queue and next neighbors
    while not (
        len(q) == 0 and len(next_level) == 0
    ):  # log(n), where n is # of nodes, and tree's balanced
        # 1st pass: enqueue the neighbors of that node (aka item)
        for node in q:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        # 2nd pass: make a LL from the nodes in the queue, add
        list_items = list()
        for node in q:
            list_items.append(q.popleft())
        lists.append(LinkedList(list_items).head)
        # enqueue the neighbors of that node (aka item)
        for node in next_level:
            q.append(next_level.popleft())
    # C: return the lists of list nodes
    return lists


"""
Manual Test:

q = [2, 5]
next_level = []
lists = [4-> , ]

list_items = [4, ]

tree = (
            4
         /     \
        2       5
      /  \        \
    1    3         7
)

Time: O(n)
Space: O(n)
"""

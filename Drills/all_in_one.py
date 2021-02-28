from collections import deque
from typing import List


# ARRAYS
class Array:
    def __init__(self, array):
        self.items = array
    '''Search Algorithms'''
    def linear_search(self, target):
        '''linear time, constant space'''
        for ndx, item in enumerate(self.items):
            if target == item:
                return ndx
        return None

    def linear_search_recursive(self, target, ndx=0):
        '''linear time and space'''
        if ndx < len(self.items):
            item = self.items[ndx]
            if item == target:
                return ndx
            else:
                return self.linear_search_recursive(target, ndx + 1)
        return None

    def bin_search_iterative(self, target):
        """self.items is assumed to be sorted in ascending order.
           logarithmic time, constant space"""
        lo = 0
        hi = len(self.items) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_elem = self.items[mid]

            if target == mid_elem:
                return mid
            elif target < mid_elem:
                hi = mid - 1
            elif target > mid_elem:
                low = mid + 1
        # not found 
        return None

    def bin_search_recursive(self, target, lo=0, hi=None):
        """logarithmic time and space"""
        if hi is None:
            hi = len(self.items) - 1
        mid = (lo + hi) // 2
        mid_elem = self.items[mid]

        if target == mid_elem:
            return mid
        elif lo > hi:
            return None
        elif target < mid_elem:
            return self.bin_search_recursive(lo, mid - 1)
        elif target > mid_elem:
            return self.bin_search_recursive(mid + 1, hi)

    '''Sorting Algorithms'''

    def insertion_sort(self) -> None:
        """this method is mutative - stable, internal, quadratic time, constant space
        - good for when you need something stable, you know the data can fit into RAM
        - and when you know it might be nearly sorted already
        """
        # first ndx is already sorted 
        for index in range(1, len(self.items)):
            # grab the element at the current index
            to_insert = self.items[index]
            to_insert_index = index
            # insert it into the proper position in the sorted part
            for index_before in range(index, -1, -1):
                elem_before = self.items[index_before]
                # swap if necessary 
                if elem_before > to_insert:
                    self.items[index_before], self.items[to_insert_index] = (
                        to_insert, elem_before
                    )
                    # update the index where the elem to insert is
                    to_insert_index = index_before

    def merge_sort(self):
        '''out of place, loglinear time'''
        pass

    def counting_sort(self):
        '''linear time (n + k, where k is the difference between min and max),
        out of place, works only with integer values
        - good for when you know beforehand the values are in a certain range
        - and that the dataset is not sparse (e.g. human ages in the Census data)
        '''

        min_elem = min(self.items)
        max_elem = max(self.items)

        frequencies = [0 for _ in range(max - min)]

        for item in self.items:
            index = item - min_elem
            frequencies[index] += 1

        sorted = list()
        for elem, count in enumerate(frequencies):
            sorted.extend([elem for _ in range(count)])

        return sorted

# Stacks and Queues
class ArrayStack(Array):
    '''top is the last index'''

    def __init__(self, array):
        super().__init__(array)

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def push(self, item):
        self.items.append(item)

    
class ArrayQueue(Array):
    '''first index of the array is the front of queue'''
    def __init__(self, array):
        super().__init__(array)

    def enqueue(self, item: int):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def front(self):
        if len(self.items) > 0:
            return self.items[0]


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item: ListNode):
        if self.head is None:
            self.head = self.tail = self.item
        else:
            self.tail.next = item
            self.tail = item
    
    def prepend(self, item: ListNode):
        if self.head is None:
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head = item

    def length(self):
        num_nodes = 0
        runner = self.head
        while runner is not None:
            num_nodes += 1
            runner = runner.next
        return num_nodes

    def find(self, item: int) -> List[ListNode]:
        '''returns the node with a given item, and the one before it'''
        prev = None
        runner = self.head

        while runner.key != item:
            prev = runner
            runner = runner.next

        return [runner, prev]

    def delete(self, item):
        deleted_item, item_before = self.find(self.tail.key)
        
        if item_before is not None:
            item_before.next = deleted_item.next
        else:   # head is being deleted
            self.head = self.tail = None
        
        # if tail is being deleted
        if deleted_item == self.tail:
            self.tail = item_before
        
        return deleted_item

    
class LinkedStack(LinkedList):
    '''the tail is the top of the stack'''
    def __init__(self):
        super().__init__()

    def peek(self):
        if self.tail is not None:
            return self.tail.key
        
    def push(self, item: int):
        self.append(ListNode(item))

    def pop(self):
        if self.tail is not None:
            self.delete(self.tail.key)


class LinkedQueue(LinkedList):
    '''the head is the front'''
    def __init__(self):
        super().__init__()

    def front(self):
        if self.head is not None:
            return self.head.key

    def enqueue(self, item):
        self.append(ListNode(item))

    def dequeue(self):
        if self.head is not None:
            self.delete(self.head.item)


"""GRAPHS"""


class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = dict()  # str - Vertex

    def add_neighbor(self, neighbor_obj):
        self.neighbors[neighbor_obj.id] = neighbor_obj

class Graph:
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.vertices = dict()  # str -> Vertex

    def add_vertex(self, vertex: Vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, v1: Vertex, v2: Vertex):
        # add the vertices to the graph
        if v1.id not in self.vertices:
            self.add_vertex(v1)
        if v2.id not in self.vertices:
            self.add_vertex(v2)
        # add the nodes as neighbors to each other
        v1.add_neighbor(v2)
        if self.is_directed is False:
            v2.add_neighbor(v1)

    def bfs(self, use_iteration=True):
        '''Time is O(V + E), space is O(V)'''
        def _bfs_iterative():
            # init collections
            q = deque()
            visited = set()
            # enqueue the first node
            if len(self.vertices) > 0:
                first = list(self.vertices.values())[0]
                q.append(first)
                # traverse the graph   
                while len(q) > 0: 
                    # visit the next node
                    node = q.popleft()
                    visited.add(node.id)
                    # enqueue its neighbors
                    for neighbor in node.neighbors.values():
                        if neighbor.id not in visited:
                            q.append(neighbor)
            # return the nodes
            return visited

        def _bfs_recursive(q=deque(), visited=set()):
            # BASE: cannot search the graph
            if len(self.vertices) == 0:
                return visited
            # BASE: start the search
            elif len(q) == 0 and len(visited) == 0:
                first = list(self.vertices.values())[0]
                q.append(first)
                return _bfs_recursive(q, visited)
            # BASE: end the search 
            elif len(q) == 0 and len(visited) > 0:
                return visited
            # RECURSIVE: hit the next node
            else:  # q is not empty
                node = q.popleft()
                visited.add(node.id)
                for neighbor in node.neighbors.values():
                    if neighbor.id not in visited:
                        q.append(neighbor)
                return _bfs_recursive(q, visited)

        if use_iteration is True:
            return _bfs_iterative()
        return _bfs_recursive()

    def dfs(self, use_iteration=True):
        '''Time is O(V + E), space is O(V)'''
        def _dfs_recursive(node, visited=set()):
            # visit the node
            visited.add(node.id)
            # push its neighbors onto the call stack
            for neighbor in node.neighbors.values():
                if neighbor.id not in visited:
                    _dfs_recursive(neighbor, visited)
            # return the nodes
            return visited
        
        def _dfs_iterative():
            # init collections
            stack = list()
            visited = set()
            if len(self.vertices) > 0:
                # find the first node
                first = list(self.vertices.values())[0]
                stack.append(first)
                # traverse
                while len(stack) > 0:
                    # visit this node
                    node = stack.pop()
                    visited.add(node.id)
                    # push its neighbors onto the stack
                    for neighbor in node.neighbors.values():
                        if neighbor.id not in visited:
                            stack.append(neighbor)
            # return the nodes
            return visited

        if use_iteration is True:
            return _dfs_iterative()
        first = list(self.vertices.values())[0]
        return _dfs_recursive(first)
        

if __name__ == "__main__":
    ids = ['A', 'B', 'C', 'D', 'E']
    vertices = [Vertex(identifier) for identifier in ids]

    g = Graph()
    g.vertices = dict(zip(ids, vertices))
    """
    Adding a graph like the following:
    'A'
    |
    'B'------'C'
    |        |
    'D'     'E'
    """
    g.add_edge(vertices[0], vertices[1])  # A - B
    g.add_edge(vertices[1], vertices[3])  # B - D
    g.add_edge(vertices[1], vertices[2])  # B - C
    g.add_edge(vertices[2], vertices[4])  # C - E
    print(f"BFS iteratively: {g.bfs()}")
    print(f"BFS recursively: {g.bfs(use_iteration=False)}")
    print(f"DFS iteratively: {g.dfs()}")
    print(f"DFS recursively: {g.dfs(use_iteration=False)}")

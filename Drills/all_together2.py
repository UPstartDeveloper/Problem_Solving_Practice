from collections import deque


class Search:
    def __init__(self, items, target):
        self.items = items
        self.target = target

    def linear(self, use_iterative=True) -> int:
        def _iterative_linear_search():
            pass

        def _recursive_linear_search():
            pass

        if use_iterative:
            return _iterative_linear_search()
        return _recursive_linear_search()


class Sorting:
    pass


class ListNode:
    pass


class LinkedList:
    """good to use for either a queue or a stack -
    head and tail pointers
    """

    pass


class DoublyNode:
    pass


class DoublyLinkedList:
    """good to implement a deque"""

    pass


class Vertex:
    def __init__(self, id: str):
        self.id = id
        self.neighbors = dict()  # str: id -> Vertex


class Graph:
    """adjacency list"""

    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.vertices = dict()

    def bfs_iter(self):
        # A: first node
        first = list(self.vertices.values())[0]
        # B: traverse
        q = deque([first])
        visited = set()
        while len(q) > 0:
            node = q.popleft()
            visited.add(node)
            for neighbor in node.neighbors.values():
                if neighbor not in visited:
                    q.append(neighbor)
        # C: finish
        return visited

    def bfs_recur(self, q=None, visited=set()):
        if q is None:  # init case
            first = list(self.vertices.values())[0]
            q = deque([first])
        elif len(q) == 0:  # end case
            return visited
        else:  # recursive case
            node = q.popleft()
            visited.add(node)
            for n in node.neighbors.values():
                if n not in visited:
                    q.append(n)
        # common recursive call
        return self.bfs_recur(q, visited)

    def dfs_iter(self):
        visited = set()
        stack = list([list(self.vertices.values())[0]])
        while len(stack) > 0:
            node = stack.pop()
            visited.add(node)
            for n in node.neighbors.values():
                if n not in visited:
                    stack.append(n)
        return visited


class TreeNode:
    def __init__(s):
        pass

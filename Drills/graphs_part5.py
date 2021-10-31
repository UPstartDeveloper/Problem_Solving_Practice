from collections import deque


class Vertex:
    def __init__(self, val):
        self.id = val
        self.neighbors = dict()  # id -> Vertex


class Graph:
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.vertices = dict()  # id -> Vertex

    def add_node(self, val: str):
        """Assume no two nodes allowed to have same id"""
        self.vertices[val] = Vertex(val)

    def get_node(self, val: str) -> Vertex:
        if val not in self.vertices:
            self.add_node(val)
        return self.vertices[val]

    def add_edge(self, val1: str, val2: str):
        v1, v2 = self.get_vertex(val1), self.get_vertex(val2)
        if self.is_directed is False:
            v2.neighbors[val1] = v1
        v1.neighbors[val2] = v2

    def bfs(self, use_iteration=True):

        ### HELPERS
        def _bfs_iterative():
            visited = set()
            if len(self.vertices) > 0:
                first = list(self.vertices.values())[0]
                q = deque([first])
                while len(q) > 0:
                    node = q.popleft()
                    print(node.id)
                    visited.add(node.id)
                    for neighbor in node.neighbors.values():
                        n = neighbor
                        if n not in visited:
                            q.append(n)
            # all done!
            return visited

        def _bfs_recursive(queue=deque(), visited=None):
            """if"""
            # A: init case
            if visited is None:
                visited = set()
                if len(self.vertices) > 0:
                    first = list(self.vertices.values())[0]
                    queue.append(first)
            # B: base case (all done!)
            elif len(queue) == 0:
                return visited
            # C: recursive case
            else:  # queue is not empty
                node = queue.popleft()
                visited.add(node.id)
                for n in node.neighbors.values():
                    if n not in visited:
                        queue.append(n)

            return _bfs_recursive(queue, visited)

        ### DRIVER
        if use_iteration:
            return _bfs_iterative()
        return _bfs_recursive()

    def dfs(self, use_iteration=True):
        ### HELPERS
        def _dfs_iterative():
            visited = set()
            if len(self.vertices) > 0:
                first = list(self.vertices.values())[0]
                stack = list([first])
                while len(stack) > 0:
                    node = stack.pop()
                    visited.add(node.id)
                    for n in node.neighbors.values():
                        if n not in visited:
                            stack.append(n)
            return visited

        def _dfs_recursive(node=None, visited=set()):
            # base case
            if node is None and len(self.vertices) > 0:
                first = list(self.vertices.values())[0]
                return _dfs_recursive(node=first, visited=visited)
            # recursive case:
            elif node is not None:
                visited.add(node.id)
                for n in node.neighbors.values():
                    if n not in visited:
                        _dfs_recursive(n, visited)
            # all done!
            return visited

        ### DRIVER
        if use_iteration:
            return _dfs_iterative()
        return _dfs_recursive()

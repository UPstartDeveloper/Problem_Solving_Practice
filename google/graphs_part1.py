from collections import deque


class Vertex:
    def __init__(self, val: int):

        self.val = val
        self.neighbors = dict()


class Graph:
    """Assumes all nodes have unique int IDs."""

    def __init__(self, is_directed=False):

        self.is_directed = is_directed
        self.vertices = dict()  # int -> Vertex

    def dfs(self, use_iterative=True):
        """Return a set of all unique values in the graph
        Assumes all vertices connected. Cycles are possible.
        """

        ### HELPERS
        def _dfs_iterative(visited):
            first = list(self.vertices.values())[0]
            stack = list([first])

            while len(stack) > 0:

                node = stack.pop()

                visited.add(node.val)

                for neighbor in node.neighbors.values():
                    if neighbor.val not in visited:
                        stack.append(neighbor)

            return visited

        def _dfs_recursive(node, visited):
            # Base: first call
            if node is None:
                first = list(self.vertices.values())[0]
                return _dfs_recursive(first, visited)
            # recursive case: continue DFS
            else:
                visited.add(node.val)
                for neighbor in node.neighbors.values():
                    if neighbor.val not in visited:
                        _dfs_recursive(neighbor, visited)

        ### DRIVER
        visited = set()

        if use_iterative:
            _dfs_iterative(visited)
        else:
            _dfs_recursive(None, visited)

        return visited

    def bfs(self):
        """
        Returns set of all unique node values.
        Assumes all nodes are connected. 
        cycles are allowed.
        """

        visited = set()
        first = list(self.vertices.values())[0]
        queue = q = deque([first])

        while len(q) > 0:
            node = q.popleft()  # dequeue from the front
            visited.add(node.val)
            for neighbor in node.neighbors.values():
                if neighbor.val not in visited:
                    q.append(neighbor)

        return visited

    def has_path(self, node1: int, node2: int) -> bool:
        """
        Returns whether or not node1 and node2 
        (represented by their unique int ids)
        are in the same connected component.
        """
        ### HELPERS
        def _dfs():
            visited = set()
            stack = list([self.vertices[node1]])

            while stack:
                node = stack.pop()
                visited.add(node.val)

                # early exit
                if node.val == node2:
                    break

                for neighbor in node.neighbors.values():
                    if neighbor.val not in visited:
                        stack.append(neighbor)

            return visited

        ### DRIVER
        # guard clauses: check if node1 and node2 in the graph
        if node1 not in self.vertices or node2 not in self.vertices:
            return False
        # DFS the component that node1 is in
        node1_component = _dfs()  # iterative DFS
        # check that both nodes are in the visited set
        return node1 in node1_component and node2 in node1_component

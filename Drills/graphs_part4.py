from collections import deque

class Vertex:
    def __init__(self, id: str) -> None:
        self.id = id
        self.neighbors = dict()

    def __str__(self):
        return f"Vertex {self.id}"

    
class Graph:
    def __init__(self, is_directed=False):
        self.is_directed = is_directed
        self.vertices = dict()

    def add_vertex(self, vertex: Vertex):
        self.vertices[vertex.id] = vertex

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        # add to the graph
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        # add connections
        vertex1.neighbors[vertex2.id] = vertex2
        if self.is_directed is False:
            vertex2.neighbors[vertex1.id] = vertex1

    def bfs(self, is_recursive=False):

        def _bfs_recursive(q=None, visited=set()):
            # base cases
            if q is None:
                first = list(self.vertices.values())[0]
                q = deque([first])
            elif len(q) == 0:
                return visited
            # recursive case
            elif len(q) > 0:
                # pop a node
                node = q.popleft()
                # visit the node
                visited.add(node)
                print(f"Visiting {node}")
                # enqueue the (unvisited) neighbors
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        q.append(neighbor)
            # cont the BFS
            return _bfs_recursive(q, visited)

        def _bfs_iterative():
            # start BFS
            visited = set()
            first = list(self.vertices.values())[0]
            q = deque([first])
            while len(q) > 0:
                # pop a node
                node = q.popleft()
                # visit it
                visited.add(node)
                print(f"Visiting {node}")
                # enqueue the unvisited
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        q.append(neighbor)
            # return the nodes
            return visited

        if is_recursive:
            return _bfs_recursive()
        return _bfs_iterative()

    def dfs(self, is_recursive=False):

        def _dfs_recursive(node=None, visited=None):
            "TODO: test this"
            # init the DFS
            if node is None:
                first = list(self.vertices.values())[0]
                return _dfs_recursive(first, set())
            # cont. the DFS
            else:
                # visit the current node
                visited.add(node)
                print(f"Visiting {node}")
                # go to the next unvisited node
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        _dfs_recursive(neighbor, visited)
            # end the DFS
            return visited

        def _dfs_iterative():
            # A: init the DFS
            visited = set()
            first = list(self.vertices.values())[0]
            stack = list([first])
            # B: DFS
            while len(stack) > 0:
                node = stack.pop()
                visited.add(node)
                print(f"Visiting {node}")
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        stack.append(neighbor)
            return visited

        if is_recursive:
            return _dfs_recursive()
        return _dfs_iterative()


if __name__ == "__main__":
    # A: set up the graph
    v = vertices = [
        Vertex(identifier) for identifier in 
        ["A", "B", "C", "D", "E", "F"]
    ]
    g = Graph()
    g.add_edge(v[0], v[5])
    g.add_edge(v[0], v[1])
    g.add_edge(v[1], v[2])
    g.add_edge(v[2], v[3])
    g.add_edge(v[1], v[4])

    # B: Compare output of iter/rec BFS
    # g.bfs(is_recursive=True)
    # g.bfs(is_recursive=False)

    # C: Compare output of iter/rec DFS
    # g.dfs(is_recursive=True)
    g.dfs(is_recursive=False)


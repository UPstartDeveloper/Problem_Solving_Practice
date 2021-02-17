from collections import deque


class Vertex:
    def __init__(self, id: str):
        self.id = id
        self.neighbors = dict()  # id --> Vertex obj

    def add_neighbor(self, neighbor):
        '''input is an existing Vertex obj'''
        self.neighbors[neighbor.id] = neighbor
    

class Graph:
    def __init__(self, is_directed=False):
        self.vertices = dict()
        self.is_directed = self.is_directed

    def add_edge(self, v1: str, v2: str):
        if v1 not in self.vertices:
            v1_obj = self.add_vertex(v1)
        if v2 not in self.vertices:
            v2_obj = self.add_vertex(v2)
        v1_obj.add_neighbor(v2_obj)
        if self.is_directed is False:
            v2_obj.add_neighbor(v1_obj)

    def add_vertex(self, vertex_id: str):
        '''adds or updates the entry that has the vertex_id'''
        self.vertices[vertex_id] = Vertex(vertex_id)
        return self.vertices[vertex_id]

    def bfs(self, iterate=True):
        
        def _bfs_iterative(self):
            # init collections
            q = deque()
            visited = set()
            # enqueue the first vertex
            first = list(self.vertices.keys())[0]
            q.append(first)
            # traverse the graph
            while len(q) > 0:
                # dequeue a vertex
                vertex_obj = q.popleft()
                # visit the vertex
                visited.add(vertex_obj.id)
                # enqueue the neighbors
                for neighbor in vertex_obj.neighbors.values():
                    q.append(neighbor)
            # return the visited nodes
            return visited

        if iterate is True:
            return _bfs_iterative()
        # TODO: implement and call a recursive BFS implementation

    def dfs(self, iterate=True):

        def _dfs_iterative():
            # init collections
            stack = list()
            visited = set()
            # push the first node onto the stack
            first = list(self.vertices.keys())[0]
            stack.append(first)
            # traverse the graph
            while len(stack) > 0:
                # pop from the stack
                node = stack.pop()
                # visit this node
                visited.add(node)
                # push the unvisited neighbors
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        stack.append(neighbor)
            # return the visited nodes
            return visited

        def _dfs_recursive(node, visited=set()):
            # visit the node
            visited.add(node)
            # visit the neighbors
            for neighbor in node.neighbors.values():
                if neighbor not in visited:
                    _dfs_recursive(neighbor, visited)
            # return the visited nodes
            return visited
            
        if iterate is True:
            return _dfs_iterative()
        return _dfs_recursive()

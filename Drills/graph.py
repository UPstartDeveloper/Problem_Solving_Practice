from collections import deque


class Vertex:
    """Each vertiex knows its id, and can lookup all its neighbors by 
       their id.
    
    """
    def __init__(self, id: str):
        self.id = id
        self.neighbors = dict()  # maps id --> Vertex obj

    def add_neighbor(self, neighbor_obj) -> None:
        self.neighbors[neighbor_obj.id] = neighbor_obj


class Graph:
    """Representation of the Graph ADT as an adjacency matrix
       We have a dict of all the vertices, and all the vertices
       individually have a dict of all their neighbors.

    """
    def __init__(self, is_directed=False):
        self.is_directed = is_directed  # T - one way graph, and vice versa
        self.vertices = dict()

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.id] = vertex

    def add_edge(self, vertex1: Vertex, vertex2: Vertex) -> None:
        # add the edge from 1 to 2
        vertex1.neighbors[vertex2.id] = vertex2
        # if not directed, then connect 2 to 1
        if not self.is_directed:
            vertex2.neighbors[vertex1.id] = vertex1

    def _bfs(self, visit: function):
        '''Visit all the nodes in this graph in BFS order'''
        # init a queue
        q = deque()
        # enqueue the first vertex
        first = list(self.vertices.keys())[0]
        q.append(first)
        # visit all the nodes (in this component)
        while q:
            # dequeue a vertex
            vertex = q.popleft()
            # visit it
            visit(vertex)
            # enqueue all the neighbors
            for n in vertex.neighbors.values():
                q.append(n)
        return

    def find_path_recursive(self, vertex1, vertex2, visited, stack=None):
        # init a stack, if there is None
        if not stack:
            # push the start node onto the stack
            stack = list()
            stack.append(vertex1)
        # pursue all paths from vertex 1 to 2
        found = False
        if len(stack) > 0:
            # pop from the stack
            vertex = stack.pop()
            if vertex.id == vertex2.id:
                found = True
            visited.add(vertex)
            # if this is vertex2, return True
            for neighbor in vertex.neighbors.values():
                # otherwise push the next neighbor onto the stack
                if found is False and neighbor not in visited:
                    stack.append(neighbor)
                    found = self.find_path_recursive(vertex1, vertex2, stack)
                elif found is True:
                    break
        return found

    def is_path(self, vertex1, vertex2):
        # init the return value to False
        found = False
        # try to find a path
        found = self.find_path_recursive(vertex1, vertex2, set())
        # return the answer
        return found


    




    
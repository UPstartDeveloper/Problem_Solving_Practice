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

    def _bfs(self, visit):
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
        if len(stack) > 0:
            found = False
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
                    found = self.find_path_recursive(
                        vertex1, vertex2, visited, stack
                    )
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

    def is_bipartite(self) -> bool:
        """
        This tells us if the graph vertices can be split into 2 groups,
        such that no two vertices in the same group are connected

        Secret Goal: practice iterative graph BFS
        Intuition: use BFS
        Approach:
        - visit every node
            - if it has been visited before, check to make sure it's 
                the opposite color as the one just visited
                - if it hasn't, return False
            - if it has not been visited before, assign it the opposite
                color of the one just visited
        - return True

        Insights:
        - cmd + / --> comment highlighted lines in VS Code
        - even singly linked list w/ an even number of nodes is a 
            - bipartite graph

        Time: O(V + E)
        Space: O(V)
        """
        def visit(node, last_color, visited):
            valid = False
            # - if it has been visited before, check to make sure it's 
            #     the opposite color as the one just visited
            opposite_color = (1 if last_color == 0 else 0)
            if node not in visited:
                visited[node] = opposite_color
                print(f"Node {node.id} is {opposite_color}")
                valid = True
            # - if it has not been visited before, assign it the opposite
            #     color of the one just visited
            else:  # node has been visited before
                # may not be bipartite, if it was enqueued twice
                valid = (visited[node] == opposite_color)
                print(f"Already visited, Node {node.id} is {visited[node]}")
            return valid, opposite_color
        # A: init a queue, a dict of visited nodes, and first color
        color = 0
        visited = dict()
        q = deque()
        # B: enqueue the first node
        q.append(list(self.vertices.values())[0])
        # C: visit all the nodes
        while q:
            node = q.popleft()
            valid, color = visit(node, color, visited)
            # if we fail the bipartite rules, return False
            if not valid:
                return False
            # can continue traversing
            for neighbor in node.neighbors.values():
                if neighbor not in visited:  # avoid cycles
                    q.append(neighbor)
        return True

    def dfs(self):
        """Return all the vertices in this graph in a set."""
        
        def dfs_recursive(node_id, visited):
            """
            Once the function is called, 
            we know it's been pushed onto the call stack.

            Once the function terminates, 
            we know it has been popped from the stack.
            """
            # visit the node (in this stack frame)
            node_obj = self.vertices[node_id]
            visited.add(node_id)
            # push the neighbors to be traversed in future stack frames
            for neighbor_id in node_obj.neighbors:
                if neighbor_id not in visited:
                    dfs_recursive(neighbor_id, visited)
            return None

        # start from a random node
        start_node = list(self.vertices.keys())[0]
        # traverse from that node to fill the whole graph
        visited = set()
        dfs_recursive(start_node, visited)
        # return the set of all nodes
        return visited


    def dfs_iterative(self):
        """
        Print the ids of all the
        Graph vertices in DFS order, iteratively.

        ASSUMPTION: all the vertices are connected
                    and there are no two vertices with 
                    the same id
        """
        # init a stack and a dict
        stack = list()
        visited = set()
        # choose the first node
        start_node = list(self.vertices.values())[0]
        # visit all the nodes
        stack.append(start_node)
        while stack:
            # pop from the stack
            node = stack.pop()
            # visit the node
            visited.add(node.id)
            for neighbor in node.neighbors.values():
                # push all of unvisited neighbors onto the stack (prevent cycles)
                if neighbor.id not in visited:
                    stack.append(neighbor)
        # return the set of all nodes
        return visited

    def dfs_distances(self, start_node_id: str):
        """
        Returns a dictionary containing the distance
        from the starting node to all other nodes in the
        Graph, using iterative DFS.

        Assumption:
        - all vertices are unique
        - all vertices are connected

        """
        # find the first node
        if isinstance(start_node_id, str) and start_node_id in self.vertices:
            # init a stack and a distances dict
            stack, distances = list(), dict()
            # push the first node onto the stack
            start_node = self.vertices[start_node_id]
            # init the distance travelled so far
            dist_travelled = 0
            # visit all the connected nodes
            stack.append((start_node, dist_travelled))
            while stack:
                # pop from the stack
                node, dist = stack.pop()
                # "visit" - record its distance
                distances[node.id] = dist
                # push all the (unvisited) neighbors onto the stack
                for neighbor in node.neighbors.values():
                    if neighbor.id not in distances:
                        stack.append((neighbor, dist + 1))
            # return the distances
            return distances
        else:  # start node not in graph
            raise ValueError("Could not find starting node.")

    def contains_cycle(self) -> bool:
        """
        Intuition:
        Use DFS to determine if a graph contains a cycle

        Approach:
        succeed fast --> if we keep a set of visited nodes,
                         we can return True right when we 
                         fail the "not in visited" cond
        - use iterative DFS

        Assumption:
        - all the graph nodes are connected

        """
        # init the stack and a visited set
        stack, visited = list(), set()
        # push the first node
        start_obj = list(self.vertices.values())
        # visit all the nodes
        stack.append(start_obj)
        while stack:
            node = stack.pop()
            visited.add(node)
            for neighbor_obj in node.neighbors.values():
                # if a node has been seen before, return True
                if neighbor_obj not in visited:
                    stack.append(neighbor_obj)
                else:
                    return True
        # return False if no cycles
        return False
        

if __name__ == "__main__":
    # TEST CASE
    vertices = ['A', 'B', 'C', 'D']
    objs = list()
    g1 = Graph()
    for v in vertices:
        objs.append(Vertex(v))
    g1.vertices = dict(zip(vertices, objs))

    g1.add_edge(
        g1.vertices['A'], 
        g1.vertices['B']
    )
    g1.add_edge(
        g1.vertices['B'],
        g1.vertices['D']
        )
    g1.add_edge(
        g1.vertices['A'],
        g1.vertices['D']
        )
    g1.add_edge(
        g1.vertices['C'],
        g1.vertices['D']
    )
    # print(g1.is_path(
    #     g1.vertices['A'],
    #     g1.vertices['C'] 
    # ))
    # testing is_bipartite on a singly linked list
    g2 = Graph()
    objs = [
        Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D')
    ]
    g2.add_vertex(objs[0])
    g2.add_vertex(objs[1])
    g2.add_vertex(objs[2])
    g2.add_vertex(objs[3])
    g2.add_edge(
        objs[0],
        objs[1]
    )
    g2.add_edge(
        objs[1],
        objs[2]
    )
    g2.add_edge(
        objs[2],
        objs[3]
    )
    print(g2.is_bipartite())

    g3 = Graph()
    objs = [
        Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D')
    ]
    g3.add_vertex(objs[0])
    g3.add_vertex(objs[1])
    g3.add_vertex(objs[2])
    g3.add_edge(
        objs[0],
        objs[1]
    )
    g3.add_edge(
        objs[1],
        objs[2]
    )
    g3.add_edge(
        objs[2],
        objs[0]
    )
    print(objs[2].neighbors)
    print(g3.is_bipartite())

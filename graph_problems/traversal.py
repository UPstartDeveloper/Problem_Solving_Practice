from collections import deque
from typing import List


class Graph:
    def __init__(self, is_directed=False):
        self.verticies = dict()
        self.is_directed = is_directed

    def add_node(self, node: str) -> None:

        self.verticies[node] = list()

    def add_edge(self, node_a: str, node_b: str) -> None:
        self.verticies[node_a].append(node_b)
        # if the graph is undirected, the edge must be stored twice
        if self.is_directed is False:
            # go from the other direction this time
            self.verticies[node_b].append(node_a)

    def subgraph(self, start: str) -> List[str]:
        """Return all vertices in the set of connected components
        in which the starting vertex is located
                front               back
        queue = [                   ]
                  0                   last index

          enqueue - deque.popleft()
          dequeue - deque.append()
        """
        # Init a queue to hold the nodes to visit next
        queue = deque()  # O(`)
        # enqueue the starting node
        queue.append(start)  # O(1)
        # init the return value
        connected_comp = set()  # O(1)
        # perform the BFS
        # v = number of vertices overall
        # e = numbers of edges in graph
        while queue:  # v iteration
            # dequeue from the queue
            vertex = queue.popleft()  # O(1)
            # add to the set of connected_comp, if not visited before
            if vertex not in connected_comp:
                connected_comp.add(vertex)
            # enqueue all of its neighbors
            neighbors = self.verticies[vertex]
            for neighbor in neighbors:
                # prevent unnecessary iteration
                if neighbor not in queue and neighbor not in connected_comp:
                    queue.append(neighbor)
        # convert connected_comp to a list, and return
        # connected_comp = list(connected_comp) # O(v)
        return connected_comp

    def does_path_exist(self, source: str, target: str) -> bool:
        """Use DFS to find out if there is a path between two vertices.

        Parameters:
        source(str): the identifier of the Node to start the search from
        target(str): the identifier of the Node we're looking for

        Returns: bool

        """
        # init a stack to hold the nodes (bottom is index 0, top is last index)
        next_nodes = list()
        # init a set to hold nodes already visited
        visited = set()

        def search() -> bool:
            """Recursively searches the next nodes in the current path."""
            # pop from the stack
            node = next_nodes.pop()
            # visit the newest node
            visited.add(node)
            # check if it's the node we're looking for
            if node == target:
                return True
            # otherwise push each of the neighboring nodes we haven't seen yet
            path_found = False
            for next_node in self.verticies[node]:
                if next_node not in visited:
                    next_nodes.append(next_node)
                    # search again
                    path_found = search()
            # if it's never found, return False
            return path_found

        # find the root (don't assume it's in the graph)
        if source in self.verticies:
            # start our search
            next_nodes.append(source)
            # return the result
            return search()
        # return an error
        raise KeyError(f"Vertex {source} is not in the graph.")


if __name__ == "__main__":
    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_node("Z")

    """
    {
      'A': [B, C, D],
      'B': [],
      'C': [E],
      'D': [B],
      'E': [F],
      'F': [],
      'Z': [],
      
      q = [, 'C', 'D']
      cc = {'A', 'B}
      v = B
      neighbors = []
    }
    """

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")
    graph.add_edge("C", "E")
    graph.add_edge("E", "F")
    graph.add_edge("D", "B")

    print(graph.does_path_exist("A", "E"))

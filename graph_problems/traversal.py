from collections import deque
from typing import List

class Graph:
  def __init__(self):
    self.verticies = {}


  def add_node(self,node):
    self.verticies[node] = []


  def add_edge(self,node_a,node_b):
    self.verticies[node_a].append(node_b)
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
    queue = deque() # O(`)
    # enqueue the starting node
    queue.append(start) # O(1)
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
  
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

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

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')
from collections import deque
from typing import List


"""
n => n.vertices = {

}

Concepts:
- weighted, directed graph which may/may not be connected
- BFS for the shortest path

"""


class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = dict()  # str --> Vertex object, distance
        """
        
        distances = {
            1: -1,
            2: -1,
            3: -1,
            4: -1
        }
        """

    def get_farthest_distance(self, graph) -> int:
        # init a queue
        q = deque()
        # init a distances dict - everything starts -1 away
        distances = dict(  # O(N)
            zip(
                list(graph.vertices.keys()),
                [float("inf") for _ in range(len(graph.vertices))],
            )
        )
        visited = set()
        # enqueue the source node, and a distance of 0
        q.append((self, 0))
        # BFS the other nodes
        while len(q) > 0:
            # dequeue a node from the front
            vertex, distance_travelled = q.popleft()
            # visit it - add its distance to the distances dict
            if distance_travelled < distances[vertex.id]:
                # ensure that the shortest distance is added
                distances[vertex.id] = distance_travelled
            visited.add(vertex.id)
            # enqueue the neighboring nodes (increment the distance so far)
            for neighbor_obj, distance_away in vertex.neighbors.values():
                if neighbor_obj.id not in visited or (
                    distance_travelled + distance_away < distances[neighbor_obj.id]
                ):
                    q.append((neighbor_obj, distance_travelled + distance_away))
        # C: if any dist is -1 --> -1
        distances_overall = set(distances.values())
        max_distance = -1
        if float("inf") not in distances_overall:
            max_distance = max(distances_overall)
        # D: otherwise return the max distance (from the distances dict)
        return max_distance


class Graph:
    def __init__(self):
        self.vertices = dict()  # str - Vertex object

    def add_edge(self, v1, v2, length):
        # add both vertices to the graph
        if v1 not in self.vertices:
            self.vertices[v1] = Vertex(v1)
        if v2 not in self.vertices:
            self.vertices[v2] = Vertex(v2)
        # get both Vertex objects
        v1_obj, v2_obj = self.vertices[v1], self.vertices[v2]
        # add the edge between the vertices
        v1_obj.neighbors[v2] = (v2_obj, length)


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
        Output: 2

        the signal is sent out through all the edges from that node simultaneously
        K = source node (it's id)
        N = number of nodes overall

        -1 - if the node doesn't have a path to all the others

        - if it is, then return the longest path from K

        weighted directed graph, which may or may not be connected

        questions:
        are there dupes in the input? no
        - however the same vertex may appear more than once
        - am I allowed to use a deque
        - could there be cycles in the network
        # Intuition:
        - first check a path exists from to every other Vertex - find not return -1
        - then return the path that's longest (in terms of time)

        # Approach:
        - construct the graph using a custom Graph and Vertex class
        - try to find the length of time between this node K and all others (BFS)
        - if any dist is -1 --> -1
        - otherwise return the max distance
        """
        # A: construct the graph using a custom Graph and Vertex class
        network = Graph()
        for v1, v2, length in times:  # T iterations
            network.add_edge(v1, v2, length)
        # B: try to find the length of time between this node K and all others (BFS)
        src = network.vertices[K]  # O(1)
        farthest = -1  # init the farthest
        # rule for invalidating the network
        if len(network.vertices) == N:  # O(1)
            farthest = src.get_farthest_distance(network)  #
        return farthest  # can be -1 if not a connected graph


"""
Big O Analysis:

T = number of lists in the times variable
N = number of nodes in the graph
E = number of network connections

Time: O(N + E)
Space: O(N + E)
"""

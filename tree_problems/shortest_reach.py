#!/bin/python3

from collections import deque
import os

# This problem orginally comes from Hacker Rank: 
# https://www.hackerrank.com/challenges/bfsshortreach/problem
# 
# Prompt: Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s


class Graph:
    def __init__(self, n, edges):
        '''TODO: construct an adj. list'''
        # A: init the adj. list
        node_ids = [identifier for identifier in range(1, n + 1)]
        node_edges = [set() for _ in range(1, n + 1)]
        self.vertices = dict(zip(node_ids, node_edges))
        # B: add the edges
        for node1, node2 in edges:
            self.vertices[node1].add(node2)
            self.vertices[node2].add(node1)
    
    def traverse(self, start) -> list:
        # init the distances array
        distances = [-1 for _ in range(len(self.vertices))]
        # D: traverse the graph - enqueue the origin (s), and path_so_far (0)
        q = deque([(start, 0)])
        while len(q) > 0:
            # a) dequeue a node
            node, dist_so_far = q.popleft()
            # b) visit it - add the path_so_far to the distances_dict, 
            distances[node - 1] = dist_so_far
            dist_so_far += 6
            # c) for each unvisited neighbor --> enqueue it, w/ copy of updated psf
            for neighbor in self.vertices[node]:
                if distances[neighbor - 1] == -1:
                    q.append((neighbor, dist_so_far))
        return distances

def bfs(n, m, edges, s):
    """
    SOLUTION GOES HERE!!!
    ASSUME this func only worries about handling one graph
    ASSUME >=2 nodes, >=1 edge,
    ASSUME this all fits in memory
    ASSUME deques are allowed
    
    Example:
    4 2
    1 2
    1 3
    1
    
    q = [(1, [])]
    
    graph = {
        1: [2, 3],
        2: [1],
        3: [3],
        4: []
    }
    
    distances = {
        1: []
    }

    Intuition: traverse via BFS
    
    Approach:
    
    
    1) Adjacency List:
        A: construct the graph 
        B: init a dict of distances (id --> path_to_node_from_origin = -1)
        C: init a queue
        D: traverse the graph - enqueue the origin (s), and path_so_far (0)
            a) dequeue a node
            b) visit it - add the path_so_far to the distances_dict, 
            c) increment psf by 6
            c) for each unvisited neighbor --> enqueue it, w/ copy of updated psf
        E: calculate the distances 
            a) init a list of -1's x (n - 1)
            b) go in order, w/ an ndx --> look up each other node in distances 
            c) if there, update the corresponding ndx w/ the dist
        F: return the distances array
    
    Edge Cases:
    1) no edges, no nodes --> N/A
    2) dupe edges --> depends on DS, might not be a problem
    3) s is out of bounds --> raise an error? 
    """
    
    def distance_to_every_other_node(distances):
        '''returns every distance to only other nodes'''
        return [dist for dist in distances if (dist == 0) is False]
    
    # A: construct the graph 
    graph = Graph(n, edges)
    # B: traverse the graph - enqueue the origin (s), and path_so_far (0)
    distances = graph.traverse(s)
    print(distance_to_every_other_node(distances))
    # C: calculate the distances
    return distance_to_every_other_node(distances)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

from collections import deque
import math
from typing import List


class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = dict()  # id --> Vertex


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        Leetcode: https://leetcode.com/problems/largest-component-size-by-common-factor/
        
        Input/Problem:
            immutable array[int > 0].length > 0
            unsorted
            
        Output:
            return max(sizes of connected comp)
            
        Intuition:
            2 way edge
            vertex = 
                id = num
                edges = 1st degree neighbors w/ all CF > 1
                
            BFS/DFS = calculate size of connected comps
            
        EC:
           1) TODO
           
        Stepping Stone problem:
            1) how to determine GCF of two numbers
                4 and 6 ----> 2
                
                4               6
            1       4 X     1       6
            2       2       2       3
                         [2, 3]
                         [2, 2]
                2*2.   
                2*3
                CF = 2
                
                6 / 4 ----> 1.5
                
                [4,6,15,35]
                 ^       ^
        Approach:
            1) BF
                A: construct the graph - dict()
                    1) traverse nums array - place Vertex objs in the dict
                    2) do another pass -> figure out the edges
                B: BFS on each of the components ---> sizes = []
                C: return max(sizes)
        """
        ### HELPERS
        def _construct_graph(nums):
            """TODO"""
            # 1) traverse nums array - place Vertex objs in the dict
            graph = dict(zip(nums, [Vertex(num) for num in nums]))
            # 2) do another pass -> figure out the edges
            for index1 in range(len(nums)):
                num1 = nums[index1]
                vertex1 = graph[num1]
                # add the neigbors for one node
                for index2 in range(len(nums)):
                    num2 = nums[index2]
                    vertex2 = graph[num2]
                    # neighbor found
                    # if _gcf(num1, num2) > 1:  # TODO
                    if index1 != index2 and math.gcd(num1, num2) > 1:
                        vertex1.neighbors[num2] = vertex2
                        vertex2.neighbors[num1] = vertex1
            return graph

        def _calculate_comp_sizes(graph):
            """TODO: iterative BFS"""
            sizes, visited = list(), set()
            for node_id, vertex in graph.items():
                # start BFS on connect comp
                if node_id not in visited:
                    q = deque([vertex])
                    size_comp = 0
                    visited.add(node_id)
                    # compute size of the comp
                    while len(q) > 0:
                        node = q.popleft()
                        # visit the node
                        size_comp += 1
                        for neighbor_id, neighbor in node.neighbors.items():
                            if neighbor_id not in visited:
                                q.append(neighbor)
                                visited.add(neighbor_id)
                    # add size to our sizes
                    sizes.append(size_comp)
            return sizes

        ### DRIVER
        # A: construct graph
        graph = _construct_graph(nums)
        # B: BFS on each of the components ---> sizes = []
        sizes = _calculate_comp_sizes(graph)
        # C: output
        return max(sizes)

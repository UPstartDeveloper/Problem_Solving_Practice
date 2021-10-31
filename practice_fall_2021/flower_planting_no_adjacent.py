from collections import deque


class GardenVertex:
    def __init__(self, identifier):
        self.id = identifier
        self.val = None
        self.neighbors = dict()  # id --> GardenVertex


class Graph:
    def __init__(self, n, paths):
        self.gardens = dict()
        # init the graph
        for node_id in range(n):
            self.gardens[node_id + 1] = GardenVertex(node_id + 1)
        # init the edges
        for node1_id, node2_id in paths:
            self.gardens[node1_id].neighbors[node2_id] = self.gardens[node2_id]
            self.gardens[node2_id].neighbors[node1_id] = self.gardens[node1_id]

    def set_flower_values(self):
        """iterative BFS"""
        # B: BFS each component
        CHOICES = [1, 2, 3, 4]  # index = val - 1
        visited = set()
        for garden in self.gardens.values():
            if garden not in visited:
                # C: init a queue - choose a node randomly to start
                q = deque([(garden, 1)])
                # E: traversal:
                while len(q) > 0:
                    # 1): dequeue a node
                    current_garden, flower_val = q.popleft()
                    cg = current_garden
                    # 2) set the flower value on the node
                    visited.add(cg)
                    cg.val = flower_val
                    # 3) enqueue all unvisited neighbors - enqueue node object + flower value
                    neighbors = [
                        neighbor
                        for neighbor in list(cg.neighbors.values())
                        if neighbor not in visited
                    ]
                    neighbors_index, flowers_index = 0, flower_val % len(CHOICES)
                    # assign flowers to the neighbors, enqueu them
                    while neighbors_index < len(neighbors):
                        # find a flower
                        while CHOICES[flowers_index] == flower_val:
                            flower_val = (flower_val + 1) % len(CHOICES)
                        # enqueue
                        q.append((neighbors[neighbors_index], flowers_index + 1))
                        neighbors_index += 1


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
        SOLUTION NOT YET passing all test cases on Leetcode: https://leetcode.com/problems/flower-planting-with-no-adjacent 
        Input/Problem:
            undirected, unwt'd graph
            n vertices = gardens
            each vertex <= 3 edges
            gardens ---> 1 type of flower
            multiple components to graph
            can be cycles
            ASSUME a node's neighbors can havew identical vals
            
        Goal:
            no adjacent gardens have the same flowers
            
        ASSUME:
            >= 1 garden
            inputs are immmutable
            paths are valid, just between 2 garden
            no garden connects to itself
            no dupe paths given
            
        EC: 
            1) n <= 4 ---> [return the first n flowers]
            2) n > 4 ---> TODO
            3) no answer ---> ignore
            4) n is out of bounds, paths invalid --> TODO
            
        Intuition:
            graph traversal
            level-order traversal (BFS)
            
            
        Example: 
            
             n = 3, paths = [[1,2],[2,3],[3,1]]
             
             1 ----- 2
            / \
           2 - 3 
              
            
        Approach:
        
        1)
        choices = [1, 2 ,3 4]
        # A: make an adj list of all the nodes
        # B: BFS each component
            # C: init a queue - choose a node randomly to start
            # D: visited set
            # E: traversal:
                # 1): dequeue a node
                # 2) add to the visited set, 
                # 3) set the flower value on the node
                # 3: enqueue all unvisited neighbors - enqueue node object + flower value
        # F: return output - return values of all the nodes (dict.values())
        """
        ### DRIVER
        # special case:
        if n <= 4:
            return list(range(1, n + 1))
        # A: make an adj list of all the nodes
        graph = Graph(n, paths)
        # B: BFS each component
        graph.set_flower_values()  # TODO
        # F: return output - return values of all the nodes (dict.values())
        return [node.val for node in graph.gardens.values()]

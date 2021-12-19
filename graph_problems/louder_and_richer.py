from typing import List


class PersonVertex:
    def __init__(self, num, quietness):
        self.id = num
        self.q_lvl = quietness
        self.richer = dict()  # id --> vertex
        
        
class PersonGraph:
    def __init__(self, richer, quiet):
        self.quietest_cache = dict()
        self.graph = dict()  # id --> vertex
        # A: init nodes
        for index, quietness in enumerate(quiet):
            self.graph[index] = PersonVertex(index, quietness)
        # B: init the edges
        for id1, id2 in richer:
            person1, person2 = self.graph[id1], self.graph[id2]
            person2.richer[id1] = person1
            
    def find_quietest_and_richer(self, person_id):
        """TODO: iterative DFS"""
        if person_id not in self.quietest_cache:
            person = self.graph[person_id]
            lowest_quiet_level = lql = person.q_lvl
            node_id_with_lowest = niwl = person_id
            if person_id in self.graph:
                # start DFS
                stack = list([person])
                while stack:
                    node = stack.pop()
                    # visit the node
                    if node.q_lvl < lql:
                        lql = node.q_lvl
                        niwl = node.id
                    # push the neighboring
                    for neighbor_node in node.richer.values():
                        stack.append(neighbor_node)
            self.quietest_cache[person_id] = niwl
        return self.quietest_cache[person_id]
        
    def sort_by_money_and_quietness(self):
        """TODO"""
        # A: init array
        sorted_ids = [-1 for _ in range(len(self.graph))]
        # B: find most quiet for each 
        for person_id in self.graph:
            sorted_ids[person_id] = self.find_quietest_and_richer(person_id)
        # C: return arr
        return sorted_ids


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """Leetcode: https://leetcode.com/problems/loud-and-rich/
        """
        # A: make the graph
        graph = PersonGraph(richer, quiet)
        # B: provide the solution
        return graph.sort_by_money_and_quietness()

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
            # Base Case: no neighbors
            if len(person.richer) == 0:
                self.quietest_cache[person_id] = person_id
            # Recursive Case: has neighbors
            else:
                # get the quietest amongst all downstream neighbors, and self
                quietest_nodes = [
                    self.graph[self.find_quietest_and_richer(neighbor_id)]
                    for neighbor_id in person.richer
                ]
                quietest_nodes.append(person)
                # sort by quietest
                quietest_nodes.sort(key=lambda node: node.q_lvl)
                # cache the answer
                self.quietest_cache[person_id] = quietest_nodes[0].id
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

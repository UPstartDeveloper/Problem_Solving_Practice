from typing import List


class Vertex:
    def __init__(self, index, char):
        self.ndx = index
        self.cc = self.current_char = char
        self.neighbors = dict()  # index -> Vertex


class CharacterGraph:
    def __init__(self, s, pairs):
        self.string = s
        self.characters = dict()
        # add the vertex objs
        for index, char in enumerate(list(s)):
            self.characters[index] = Vertex(index, char)
        # add the edges between the vertices
        for index1, index2 in pairs:
            v1, v2 = self.characters[index1], self.characters[index2]
            v1.neighbors[v2.ndx] = v2
            v2.neighbors[v1.ndx] = v1

    def sort_comps(self) -> List[str]:
        def _dfs(visited, vertex):
            comp_visited = set()
            stack = [vertex]
            while stack:
                v = stack.pop()
                # visit
                comp_visited.add(v)
                # add neighbors
                for neighbor in v.neighbors.values():
                    if neighbor not in comp_visited:
                        stack.append(neighbor)
            # now get the smallest
            chars = [v.cc for v in comp_visited]
            indices = [v.ndx for v in comp_visited]
            # update global set
            visited.union(set([v.ndx for v in comp_visited]))
            return dict(zip(sorted(indices), sorted(chars)))

        # A: init empty array of index --> char
        sorted_chars = sc = ["" for _ in range(len(self.string))]
        # B: for each comp
        visited = set()
        index = 0
        while index < len(self.string):
            if index not in visited:
                vertex = self.characters[index]
                # 1: get all chars + indices in the comp - DFS/BFS
                smallest_order = _dfs(visited, vertex)
                # 3: sort 'em and zip 'em
                # smallest_order = dict(zip(sorted(indices), sorted(chars)))
                # 4: add them to the overall array
                for char_index in smallest_order:
                    sc[char_index] = smallest_order[char_index]
            index += 1
        # C: fill in any missing values in the array using s
        for index in range(len(sc)):
            if sc[index] == "":
                sc[index] = self.string[index]
        # D: return the array
        return sc


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Leetcode: https://leetcode.com/problems/smallest-string-with-swaps/ 
        
        Input/Problem:
            non empty - only English, immutable, lowercase
            2D array- valid indices, index --> pair, assume all unique
            assume can use sorted()
            
        Output:
            smallest perm poss (any # of swaps between in a pair)
            
        Intuition:
            dynamic prorgrammming
            heap
            
        EC:
            invalid input ---> ValueError
            all same chars / already smallest - early exit
             
        Approach:
            TODO
        
        BigO:
            TODO
        """
        # A: construct the character graph
        char_graph = CharacterGraph(s, pairs)
        # B: sort each comp
        sorted_chars = char_graph.sort_comps()  # List[str]
        # C: return the new permuations
        return "".join(sorted_chars)

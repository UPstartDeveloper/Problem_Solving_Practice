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
            v1.neighbors[v2.index] = v2
            v2.neighbors[v1.index] = v1
            
    def sort_comps(self) -> List[str]:
        # A: init empty array of index --> char
 
        # B: for each comp
            # 1: get all chars in the comp - DFS/BFS
            # 2: get all the indices in the comp
            # 3: sort 'em and zip 'em
            # 4: add them to the overall array
            
        # C: fill in any missing values in the array using s
        
        # D: return the array
        pass

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
        return ''.join(sorted_chars)

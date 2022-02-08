from string import ascii_uppercase
from typing import List


class Solution:
    """
    Suppose a spider is crawling along the edges of a tetrahedron 
    with sides ABCD and edges of length 1. 

    Shown below as an undirected graph"

    A -------------- B
    | \          /   |
    |      /  \      |
    | /            \ |
    C -------------- D
         
    
    You can assume:
        the spider starts at point A on the tetrahedron  
        at each vertex chooses its next edge at random 
            (so it has a 1/3 chance of going back along the edge it came on, 
            and a 1/3 chance of going along each of the other two).

    Given this information, find the probability that:
        after it has crawled a distance of 5, 
        it is again at point A.

    Input/Problem:
        adj. list - undirected connected graph
        immutable

    Output:
        let n = distance the spider crawls
        given n = 5, what is:
            (number of unique paths starting w/ A, that end with A) / 
            (total number of unique paths starting w/ A) ?
    
    Intuition:
        Math reasoning - b/c all paths are weighed with equal proba:
            distance   |       # paths starting with A    |   # paths starting/ending w/ A  
                n      |          total = pow(3, n - 1)   |         end = total_prev - end_prev 
                2                        3                              0
                3                        9                              3
                4                       27                              6
    GUESS:      5                       81? ✅                          9? --> why is it 21?

        Coding - backtracking algo

    EC: N/A for now

    Approach:
        1. make the graph
        2. form a list of all paths (len = 5) that start w/ A
        3. count # subset = paths end w/ A
        4. divide!
    """

    def compute_probability_of_cycle(self, length=5):
        ### MAIN
        # 1. make the graph
        tetrahedron = Tetrahedron()
        # 2. form a list of all paths (len = 5) that start w/ A
        all_paths = tetrahedron.find_paths(["A"], [], length)
        # 3. count # subset = paths end w/ A
        numerator = [path for path in all_paths if path[-1] == "A"]
        ending_with_A = len(numerator)
        print(f"All paths ending in A: {numerator}")
        # 4. divide!
        print(f"Number of 5-paths ending in A: {ending_with_A}")
        print(f"Number of 5-paths starting in A: {len(all_paths)}")
        return round(ending_with_A / len(all_paths), 4)


class Vertex:
    def __init__(self, val: str):
        self.id = val
        self.neighbors = dict()  # str --> Vertex


class Tetrahedron:
    """an undirected graph, all nodes connected"""

    def __init__(self, size=4):
        self.vertices = dict()  # str --> Vertex
        # add vertices
        for id_ndx in range(size):
            letter = ascii_uppercase[id_ndx]
            self.vertices[letter] = Vertex(letter)
        # connect vertices
        for letter, vertex in self.vertices.items():
            for other_letter, other_vertex in self.vertices.items():
                if vertex != other_vertex and other_letter not in vertex.neighbors:
                    self.add_edge(vertex, other_vertex)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        vertex1.neighbors[vertex2.id] = vertex2
        vertex2.neighbors[vertex1.id] = vertex1

    def find_paths(self, current: List[str], all_paths: List[List[str]], stop_length:int):
        # Base Case: done with 1 current path
        if len(current) == stop_length:
            all_paths.append(current[:])
        # Recursive Case: need to fill out the current path
        else:  # len(current) < stop_length
            last_added_vertex = self.vertices[current[-1]]
            # find all possible paths "downstream" from where we at
            for neighbor_letter in last_added_vertex.neighbors.keys():
                current.append(neighbor_letter)
                self.find_paths(current, all_paths, stop_length)
                current.pop()
        return all_paths


if __name__ == "__main__":
    solver = Solution()
    print(solver.compute_probability_of_cycle(5))

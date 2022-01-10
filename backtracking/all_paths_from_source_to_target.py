from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Leetcode: https://leetcode.com/problems/all-paths-from-source-to-target/
        
        Input/Problem:
            adj list (no empty)
            DAG
            unique connections for each node
            vertices = indices
            edges = values in list
            no self-loops
            immutable
            
        Output:
            2D list of paths (0 ---> n -1)
            
        Intuition:
            backtracking - BFS
            
        EC:
            1) invalid inputs - ValueError:
                size of graph is off
                self-loops
                duplicates
                no DAG
            2) TODO
            
        Approach:
            1) Backtracking:
            
            
        CODE TRACE:
            current_path = [0] 
            all_paths = [[0, 1, 3], ]
            current_node = 0
            
        Complexity Analysis:
            let n = # of nodes in graph
            let e = # of edges in the graph
            
            Time - O(n * (n + e)): 
                b/c we need to traverse every edge between all the nodes to find all the paths, and then use at most n calls to add it into the all_paths variable.
            
            Space - O(n * n):
                b/c we need to store up to n paths in the all_paths variable, and the length of those paths may contain up to n items
        """
        ### HELPER
        def _find_all_paths(current_path, all_paths, current_node):
            # Base Case: when path is complete:
            if current_node == len(graph) - 1:  # 3
                current_path.append(current_node)
                all_paths.append(current_path[:])

            # Recursive: keep traversing
            else:
                # visit the current_node
                current_path.append(current_node)
                # recurse on the node's neighbors
                for neighbor_node in graph[current_node]:
                    _find_all_paths(current_path, all_paths, neighbor_node)
                    # backtrack - rm the neighor just added
                    current_path.pop()

            # Output: all done!
            return all_paths

        ### DRIVER
        return _find_all_paths([], [], 0)

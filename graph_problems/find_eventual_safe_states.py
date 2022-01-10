from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Leetcode: https://leetcode.com/problems/find-eventual-safe-states/
        
        Input:
            adj list of a digraph
            non empty
            int
            immutable 
            
            terminal = no edges
            safe = terminal, OR only --> terminal
            
            CAN be cyclical
            
            Reasons for Unsafe Node:
                - one of its paths is cycle
            
        Output:
            sorted arr
            safe node ids
            
        Intuition:
            DFS/BFS
            
        EC:
            - invalid edges
            - invalid node ids
            - no terminal nodes?
            - empty or too big graph
        
        Approach:
        
            1) DIY
            
                A: init safe_ids = []
                
                B: for node_id
                    
                    TODO: is_safe(node_id) --> T/F --> add to safe_ids
                    
                C: return safe_ids
                            
        """
        ### HELPER
        def is_safe(node_id, visited) -> bool:
            """iter DFS to check if any path is cyclical - fail fast"""
            if node_id in visited:
                return False
            visited.add(node_id)
            # push neighbors - check if visited
            for neighbor_id in graph[node_id]:
                if is_safe(neighbor_id, visited) is False:
                    return False
                elif neighbor_id in visited:
                    visited.remove(neighbor_id)
            return True

        ### MAIN
        safe_ids = list()
        for node_id in range(len(graph)):
            if is_safe(node_id, set()):
                safe_ids.append(node_id)
        return safe_ids

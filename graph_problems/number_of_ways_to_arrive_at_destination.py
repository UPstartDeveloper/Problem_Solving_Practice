from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        LeetCode: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
        
        Input:
            graph
                n vertices = intersections
                edges = roads, undirected
                weighted by time 
                ASSUME a path between any two vertices
                ASSUME less intersections means less time overall
                ASSUME no dupelicate edges in roads
                
        Output:
            min(time) ---> # of ways to do this 
            
        Intuition:
            BFS
            backtracking (DFS) - exhaust all routes between 0 --> n-1
            
        Approach:
            1) recursive DFS
                
                1. construct Graph as adj list
                2, init time_num_paths = {}
                3. for all 0.neighbors:
                    a. visited = set()
                    b. stack = [0, time_so_far = 0]
                    c. traverse (recursive_DFS):
                        stack.pop()
                        visit: visited.add(node)
                        if node == target:
                            time_num_paths.add(time_so_far)
                        else:
                            push_neighbors:
                                check if not visited_already
                                    optimization: if neighbor is the destination:
                                        time_num_paths.add(time_so_far + road_time) --> break
                                    else: stack.push(neighbor, time_so_far + road_time) ---> _recurse()
                                remove_node from visited
                4. find min_time in time_num_paths
                5. return len(time_num_paths[min_time])

                    
        """
        ### HELPERS
        def _construct_graph(n, roads):
            graph = dict()
            # init nodes
            for node_id in range(n):
                graph[node_id] = list()
            # add edges between nodes
            for node1, node2, time in roads:
                graph[node1].append((node2, time))
                graph[node2].append((node1, time))
            # all done!
            return graph
            
        def add_time(node_id, time_so_far, visited):
            if time_so_far in self.time_num_paths:  
                self.time_num_paths[time_so_far] += 1
            elif time_so_far not in self.time_num_paths:
                self.time_num_paths[time_so_far] = 1
                
        def _dfs(node_id, time_so_far, visited):
            # visit
            visited.add(node_id)    
            # keep going
            for neighbor_id, road_time in graph[node_id]:
                # check if not visited_already
                if neighbor_id not in visited:
                    new_time = time_so_far + road_time
                    # optimization: if neighbor is the destination:
                    if neighbor_id == (n - 1):
                        add_time(neighbor_id, new_time, visited)
                        # break
                    else:
                        _dfs(neighbor_id, new_time, visited)
            # remove_node from visited
            visited.remove(node_id)
                            
                
        ### MAIN
        # 1. construct Graph as adj list
        graph = _construct_graph(n, roads)  # TODO
        # 2. find all the times of all paths between 0 --> n- 1
        self.time_num_paths = dict()
        _dfs(0, 0, set()) 
        # 3. find min_time in time_num_paths
        min_time = min(self.time_num_paths.keys())
        return self.time_num_paths[min_time]
        
        

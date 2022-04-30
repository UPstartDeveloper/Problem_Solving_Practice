from collections import deque


class Node:
    # Definition for a Node.
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        """
        LeetCode: https://leetcode.com/problems/clone-graph/
        
        ASSUME all node values are unique ids 
        
        BFS:
            init visited set
            init clone --> {}
            init queue --> first node
            traverse graph:
                dequeue a node
                "visit"
                    add/get in the clone: node.val --> Node(val)
                    add node to visited set
                enqueue the unvisited neighbors
                    ALSO
                        add/get node in clone, 
                        make the same edge in the clone (2-way)
            return clone[1]  # first node
        
        """
        ### HELPERS
        def _bfs(node):
            """assuming node is not None, has a val == 1"""
            clone, q, visited = dict(), deque([node]), set()
            while q:
                node = q.popleft()
                # "visit"
                visited.add(node)
                if node.val not in clone:
                    clone[node.val] = Node(node.val)
                cloned_node = clone[node.val]
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)  # prevent duplicate enqueues
                    if neighbor.val not in clone:
                        clone[neighbor.val] = Node(neighbor.val)
                    cloned_neighbor = clone[neighbor.val]
                    # we'll come back to this "street"; make it 1-way for now
                    cloned_node.neighbors.append(cloned_neighbor)
            return clone

        ### MAIN
        if node is not None:
            # A: generate adj list
            clone = _bfs(node)
            return clone[1]  # int --> Node

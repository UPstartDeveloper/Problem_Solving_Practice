from collections import deque
from typing import List, Set

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Input/Problem:
            list of accounts
            first cols - first names (just English, lower + upper)
            jagged matrix
            >= 1 valid unique email in acct
            
            merge - same first name, >= 1 common email ----> mergesort the unique
            
            ASSUME immutable
            ASSUME name comp - case sensitive
            
        Output:
            return the merged accts - any order
            
        Intuition:
            set - intersection
            sorting - built-in sort
            
        EC:
            TODO
            
        Approach:
            
            1) DIY
                1) Check if there is a merge needed:
                    hashmap the 1st col - see if dupe names - {name: [row_indices]}
                    if not ----> return input
                2) if dupe names ---> merging:
                    init output = []
                    
                    make merges:
                        if name has 1 row - sort emails, put in the output
                        if > 1 row:
                            disjoint set - so init all emails that belong together
                            make a 2D list -- cast as a list, sort, add the name at beginning
                            extend output by each merged acct in the 2D list
                
                3) return output        
        
        Example:
            [["John","johnsmith@mail.com","john_newyork@mail.com"],
             ["John","johnsmith@mail.com","john00@mail.com"],
             ["Mary","mary@mail.com"],
             ["John","johnnybravo@mail.com"]]
             
        {
            John: [0, 1, 3]
            Mary: [2]
        }
        
        ["John","johnsmith@mail.com","john_newyork@mail.com"], 
        ["John","johnsmith@mail.com","john00@mail.com"],       
        ["John","johnnybravo@mail.com"]  <
        
        buckets =  [
            {"johnsmith@mail.com","john_newyork@mail.com", "john00@mail.com"} Jogn
            {johnnybravo@mail.com"}
        ]
        
        Graph
            vertex = email, name
            edges = other emails in the same name
            
        Adj:
            johnsmith@mail.com ----john_newyork@mail.com ---- john00@mail.com"
            [ John ] + sorted([email1, 2, ...])
        """       
        ### DRIVER
        # A: make the graph
        accounts_graph = AccountGraph(accounts)  # TODO
        # B: BFS on each component - collect emmails for each unique person
        name_emails_merged = accounts_graph.traverse()  # TODO
        # C: return the output
        return name_emails_merged
    

class Vertex:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.neighbors = dict()  # email ---> Vertex
        

class AccountGraph:
    def __init__(self, accounts):
        self.graph = dict()
        # A: TODO[test]: traverse each row in matrix
        for a in accounts:
            name = a[0]
            # B: make new vertex object for all new emails
            emails = a[1:]
            new_emails = [
                email for email in emails
                if email not in self.graph
            ]
            new_vertices = [
                Vertex(email, name) for email in new_emails
            ]
            # C: add to the .graph property!
            for v in new_vertices:
                self.graph[v.email] = v
            # D: connect adj. vertices togheter as neighbirs
            for index, email in enumerate(emails[:-1]):
                vertex = self.graph[email]
                next_vertex = self.graph[emails[index + 1]]
                vertex.neighbors[next_vertex.email] = next_vertex
                next_vertex.neighbors[vertex.email] = vertex
                
    def traverse(self):
        ### HELPERS
        def _bfs(vertex) -> Set[Vertex]:
            """return a set of Vertex objs"""
            locally_visited = lv = set()
            q = deque([vertex])
            while q:
                node = q.popleft()
                lv.add(node)
                for neighbor in node.neighbors.values():
                    if neighbor not in lv:
                        q.append(neighbor)
            return lv

        ### DRIVER
        # A: init output array
        output = list()
        # B: traverse all the components
        visited = set()
        for email, vertex in self.graph.items():
            if vertex.email not in visited:
                # 1: BFS a component ---> set of all emails
                vertices_local_components = _bfs(vertex)  # TODO
                # 2: add a new "merged" account to the output (sorted)
                emails = [v.email for v in vertices_local_components]
                merged_acct = [vertex.name] + sorted(emails)
                output.append(merged_acct)
                # 3: keep track of all globally visited 
                for email in emails:
                    visited.add(email)
        # C: return output
        return output

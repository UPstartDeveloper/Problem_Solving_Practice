from collections import deque

class BinaryTreeNode:

    def __init__(self, key) -> None:
        self.key = key
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def bfs(self, use_iteration=True):

        def _bfs_iterative():
            # A: init queue 
            q = deque()
            # B: add first node
            if self.root is not None:
                q.append(self.root)
                # C: traverse tree
                while len(q) > 0:
                    # D: dequeue a node
                    node = q.popleft()
                    print(f'Visiting: {node.key}')
                    # E: enqueue the children 
                    if node.left: 
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        def _bfs_recursive(q=None):
            # Init queue
            if q is None and self.root is not None:
                q = deque([self.root])
            # Base Case - traversal ends
            elif len(q) == 0:
                return
            # Recursive Case - cont. traversal
            elif len(q) > 0:
                node = q.popleft()
                print(f"Visiting: {node.key}")
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return _bfs_recursive(q)

        if use_iteration is True:
            return _bfs_iterative()
        return _bfs_recursive()
    
    def dfs_inorder(self, use_iteration=True):

        def _recursive(node=self.root):
            if node is not None:
                if node.left:
                    _recursive(node.left)
                print(f"visit: {node.key}")
                if node.right:
                    _recursive(node.right)

        def _iterative():
            node = self.root
            stack = list()
            while node is not None or len(stack) > 0:
                if node is not None:
                    stack.append(node)
                    node = node.left
                else:  # node is None
                    node = stack.pop()
                    print(f"Visiting: {node.key}")
                    node = node.right
        pass


class BacktrackingPatterns:
    def permutations(self, nums):
        def backtracking_helper(current_perm, all_perms, remaining):
            # Base: reached the end of the permutations]
            if len(current_perm) == len(nums):
                all_perms.append([element for element in current_perm])
                return
            # Recursive Case: not yet the end
            else:
                # iterate through the other possibilities
                for index in range(len(remaining)):
                    # add the next number ot the current perm
                    current_perm.append(remaining[index])
                    # get the remaining numbers, and cont. backtracking
                    new_remaining = [
                        elem for i, elem in enumerate(remaining)
                        if i != index
                    ]
                    backtracking_helper(current_perm, all_perms, new_remaining)
                    # reset to before the number was added
                    current_perm.pop(-1)

            pass
        # A: init a list for the current permutation
        cp = list()
        # B: init a list to hold all the permutations
        ap = list()
        # C: exhaust all permutations
        backtracking_helper(cp, ap, nums)
        # D: return the permutations
        return ap


class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = dict()  # id -> Vertex

    def add_neighbor(self, neighbor: "Vertex"):
        self.neighbors[neighbor.id] = neighbor

    def get_neighbors(self):
        return list(self.neighbors.values())


class Graph:
    def __init__(self, is_directed=False):
        self.vertices = dict()  # id --> Vertex
        self.is_directed = is_directed

    def get_first(self):
        return list(self.vertices.keys())[0]

    def bfs(self):
        # init collections 
        q = deque()
        visited  = set()
        # enqueue first Vertex
        first = self.get_first()
        q.append(first)
        # traverse
        while q:
            # dequeue a node
            node = q.popleft()
            # visit
            print(f"Visiting: {node.key}")
            visited.add(node)
            # enqueue the neighbors
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    q.append(neighbor)

    def dfs(self, use_iter=True):

        def _dfs_recursive(node=None, visited=set()):
            # if using recursion, init first node
            if node is None:
                node = self.get_first()
            # otherwise visit this node
            print(f"Visiting: {node.id}")
            visited.add(node)
            # add the next nodes to traverse (avoid cycles)
            for neighbor in node.get_neighbors():
                _dfs_recursive(neighbor, visited)

        def _dfs_iterative():
            # init collections
            stack = list()
            visited = set() 
            # push first node
            first = self.get_first()
            stack.append(first)
            # traverse the graph!
            while len(stack) > 0:
                # pop a node
                node = stack.pop()
                # visit it
                Graph.visit(node)
                # push the neighboring nodes
                for neighbor in node.get_neighbors():
                    if neighbor not in visited:
                        stack.append(neighbor)

        if use_iter is True:
            return _dfs_iterative()
        return _dfs_recursive()

    @classmethod
    def visit(cls, node):
        print(f"Visiting: {node.key}")

    def classify_connection(self, user1, user2):
        """
        Given two vertices in an undirected graph,
        return whether they are either 1st, 2nd, or 3rd 
        degree connections (assuming they are connected).
        """
        # A: init distances dict
        distances = dict()
        # B: init queue
        q = deque([(user1, 0)])
        # C: traverse the graph 
        while len(q) > 0:
            # dequeue a node
            user, distance = q.popleft()
            # put its dist in the dictionary
            distances[user] = distance
            # stop if user found
            if user2 in distances:
                break
            # enqueue the neighbors (update the distance)
            for neighbor in user.neighbors.values():
                q.append((neighbor, distance + 1))
        # D: return the msg corresponding to the dist found
        pass

    def get_second_third_degree(self, origin_user):
        """Given a vertex in an undirected graph, 
           find and return all the vertices
           that are 2 and 3 degrees away.


           user = Vertex<'Abby', connections = {}>
           ||
           Bobby-------Jasmine
           |
           |
           Zain

           ==> {
               degrees: [neighbor]
                2: ["Zain", "Jasmine"],
                3: []
               }

            Intuition: BFS

            Approach
            - do a BFS from the user Vertex
            - distances dict: mmeasure the degrees
            - return all 
            linear time and space complexi

            Edge Cases:
            1- no 2nd and/or no 3rd degree
            2- user is not a Vertex - raise ValueError

        """

        def find_neighbors(q):
            degrees_nodes = dict()
            visited = set()
            # B: helper func distances dict: mmeasure the degrees
            while len(q) > 0:
                # popping a user
                degrees_away, user = q.popleft()
                visited.add(user)
                # place in the dict
                if degrees_away in degrees_nodes:
                    degrees_nodes[degrees_away].append(user)
                else:  # init the key-value pair
                    degrees_nodes[degrees_away] = [user]
                # adding all their neighbors to the queue
                degrees_away += 1
                for neighbor in user.neighbors.values():
                    if neighbor not in visited and degrees_away < 4:
                        q.append((degrees_away, neighbor))
            return degree_nodes

        def get_2nd_3rd_degree_connections(degree_nodes):
            close_neighors = dict()
            for degree in (2, 3):
                close_neighors[degree] = degree_nodes[degree]
            return close_neighors

        # A: do a BFS from the user Vertex
        q  = deque([(0, origin_user)])
        # B: find all the neighboring nodes within 3 degrees
        degree_nodes = find_neighbors(q)
        # C: return connection in 2nd and 3rd degree
        return get_2nd_3rd_degree_connections(degree_nodes)



if __name__ == "__main__":
    bt = BacktrackingPatterns()
    print(bt.permutations([1, 2, 3, 4]))

import deque

"""TREES"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None


class Tree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def bfs(self, use_iteration=True):
        '''Visits all the nodes and prints them.'''

        def _bfs_iterative():
            # A: init a queue
            q = deque()
            # B: enqueue the root 
            if self.root is not None:
                q.append(self.root)
                # C: traverse the tree 
                while len(q) > 0:
                    # visit the node at front of the queue
                    node = q.popleft()
                    print(f"Visiting Node w/ Key: {node.key}")
                    # enqueue the children nodes
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.left)
        
        def _bfs_recursive(q=None):
            # Base Case: need to enqueue the root
            if q is None:
                # init the q for the recursive implementation
                q = deque()
                if self.root is not None:
                    q.append(self.root)
                # continue the traversal
                return _bfs_recursive(q)
            # Recursive Case: every step after the root is added
            elif len(q) > 0:
                # visit the node
                node = q.popleft()
                print(f"Visiting Node w/ Key: {node.key}")
                # enqueue the children nodes
                if node.left:
                        q.append(node.left)
                if node.right:
                    q.append(node.left)
                return _bfs_recursive(q)

        if use_iteration is True:
            return _bfs_iterative()
        return _bfs_recursive()

    def dfs(self, order='in_order'):

        def _inorder(use_iteration=True):

            def __inorder_iterative():
                pass

            def __inorder_recursive(node=self.root):

                # traverse the left subtree
                if node and node.left:
                    __inorder_recursive(node.left)
                # visit the current node
                if node:
                    print(f"Visiting Node w/ Key: {node.key}")
                # traverse the right subtree
                if node and node.right:
                    __inorder_recursive(node.right)
                
            return __inorder_recursive()

        def _preorder(use_iteration=True):

            def __inorder_iterative():
                pass

            def __preorder_recursive(node=self.root):
                
                # visit the current node
                if node:
                    print(f"Visiting Node w/ Key: {node.key}")
                # traverse the left subtree
                if node and node.left:
                    __preorder_recursive(node.left)
                # traverse the right subtree
                if node and node.right:
                    __preorder_recursive(node.right)
                
            return __preorder_recursive()

        def _postorder(use_iteration=True):

            def __postorder_iterative():
                pass

            def __postorder_recursive(node=self.root):
                if node is not None:
                    # traverse the left subtree
                    __postorder_recursive(node.left)
                    # traverse the right subtree
                    __postorder_recursive(node.right)
                    # visit this node
                    print(f"Visiting Node w/ Key: {node.key}")
            return __postorder_recursive()
        
        if order == 'in_order':
            return _inorder()


"""GRAPHS"""


class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = dict()  # str --> Vertex obj

    
class Graph:
    def __init__(self, is_directed=False):
        self.vertices = dict()  # id --> Vertex
        self.is_directed = is_directed

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.id] = vertex

    def add_edge(self, v1: Vertex, v2: Vertex):
        # add both v1 and v2 to the graph
        if v1.id not in self.vertices:
            self.add_vertex(v1)

        if v2.id not in self.vertices:
            self.add_vertex(v2)
        # add the edge from v1 -> v2
        v1.neighbors[v2.id] = v2
        # add the edge from v2 -> 1
        if self.is_directed is False:
            v2.neighbors[v1.id] = v1

    def _bfs_iterative(self):
        '''Assumes all the vertices are connected. And visits by just printing'''
        if len(self.vertices) > 0:
            # A: init collections
            q = deque()
            visited = set()
            first_vertex_obj = list(self.vertices.values())[0]
            q.append(first_vertex_obj)
            # B: traverse the graph
            while q:
                # C: dequeue a node
                node = q.popleft()
                # D: visit the node
                print(f"Visiting node w/ id: {node.id}")
                visited.add(node)
                # E: enqueue the neighbors
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        q.append(neighbor)

    def _bfs_recursive(self, q=None, visited=None):
        # Base: init collections
        if not q:
            q = deque()
            visited = set()
            first = list(self.vertices.values())[0]
            q.append(first)
            return self._bfs_recursive(q, visited)
        # RC: visit the next node 
        else:
            node = q.popleft()
            print(f"Visiting node w/ key: {node.id}")
            visited.add(node)
            for neighbor in node.neighbors.values():
                if neighbor not in visited:
                    q.append(neighbor)
            return self._bfs_iterative(q, visited)

    def dfs_iterative(self):
        '''Assumes all the nodes are connected. Visits by printing.'''
        if len(self.vertices) > 0:
            # A init collections
            visited = set()
            stack = list()
            # B: push the first node, and traverse from there
            first = list(self.vertices.values())[0]
            stack.append(first)
            while stack:
                # C: pop from the stack
                node = stack.pop()
                # D: visit that node
                print(f"Visiting node w/ key: {node.id}")
                visited.add(node)
                # E: push the neighbors
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:  # prevents cycles
                        stack.append(neighbor)

    def dfs_recursive(self, node=None, visited=None):
        # Base Case: init collections
        if node is None and visited is None:
            first = list(self.vertices.values())[0]
            visited = set()
            return self.dfs_recursive(first, visited)
        # Recursive Case: visit this node, and keep traversing
        else:
            print(f"Visiting node w/ key: {node.id}")
            visited.add(node)
            for neighbor in node.neighbors.values():
                if neighbor not in visited:
                    self.dfs_recursive(neighbor)

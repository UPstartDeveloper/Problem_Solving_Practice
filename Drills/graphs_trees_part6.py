from collections import deque

class TreeNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left, self.right = None, None


class BinaryTree:
    def __init__(self):
        self.root = None  # TreeNode

    def dfs(self, iterative=True, method='inorder'):
        ### HELPERS
        def _inorder_recursive(node=self.root, visited=set()):
            if node:
                _inorder_recursive(node.left, visited)
                visited.add(node.key)
                _inorder_recursive(node.right, visited)

        def _inorder_iterative():
            visited = set()
            node, stack = self.root, list()
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:  # stack.length > 0
                    node = stack.pop()
                    visited.add(node.key)
                    node = node.right
            return visited

        def _preorder_recursive(node=self.root, visited=set()):
            if node:
                visited.add(node.key)
                _preorder_recursive(node.left, visited)
                _preorder_recursive(node.right, visited)

        def _preorder_iterative():
            pass

        def _postorder_recursive(node=self.root, visited=set()):
            if node:
                _postorder_recursive(node.left, visited)
                _postorder_recursive(node.right, visited)
                visited.add(node.key)

        def _postorder_iterative():
            pass

        ### MAIN
        functions = {
            'inorder': [_inorder_recursive, _inorder_iterative],
            'preorder': [],
            'postorder': []
        }

        return functions[method][int(iterative)]()

    def bfs(self, iterative=True):
        def _bfs_iterative():
            visited = set()
            if self.root:
                q = deque([self.root])
                while q:
                    node = q.popleft()
                    visited.add(node.key)
                    for n in [node.left, node.right]:
                        q.append(n)
            return visited

        def _bfs_recursive():
            pass

        if iterative:
            return _bfs_iterative()
        return _bfs_recursive()


class Vertex:
    def __init__(self, key: str):
        self.key = key
        self.neighbors = dict()  # key --> Vertex

    def add_neighbor(self, other: "Vertex"):
        if other.key not in self.neighbors:
            self.neighbors[other.key] = other


class Graph:
    def __init__(self, is_directed=False):
        self.vertices = dict()  # str --> Vertex

    def bfs(self, iterative=True):
        ### HELPERS
        def _bfs_iterative(self):
            q, visited = deque(), set()
            first = list(self.vertices.values())[0]
            q.append(first)
            while len(q) > 0:
                node = q.popleft()
                visited.add(node)
                for neighbor in node.neighbors.values():
                    if neighbor not in visited:
                        q.append(neighbor)
            return {node.id for node in visited}

        def _bfs_recursive(self):
            pass

        ### MAIN
        if iterative:
            return _bfs_iterative()
        return _bfs_recursive()
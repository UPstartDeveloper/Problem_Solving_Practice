from collections import deque

class BinaryTreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def bfs(self, is_recursive=False):
        def _bfs_iterative():
            visited = set()
            if self.root is not None:
                q = deque([self.root])
                while len(q) > 0:
                    node = q.popleft()
                    visited.add(node)
                    for neighbor in [node.left, node.right]:
                        if neighbor is not None:
                            q.append(neighbor)
            return visited

        def _bfs_recursive(visited=set(), queue=None):
            q = queue
            # base case - queue is empty
            if queue is not None and len(queue) == 0:
                return visited
            # init case - queue is not yet created
            elif queue is None:
                queue = deque()
                if self.root is not None:
                    q.append(self.root)
            # recursive - adding nodes to the queue
            elif len(queue) > 0:
                node = queue.popleft()
                visited.add(node)
                for neighbor in [node.left, node.right]:
                    if neighbor is not None:
                        queue.append(neighbor)
            return _bfs_recursive(visited, q)
        
        if is_recursive:
            return _bfs_recursive()
        return _bfs_iterative()

    def dfs(self, type, is_recursive: bool):
        ### DFS HELPER FUNCTIONS 
        def _in_order_recursive(node=None, visited=None):
            if visited is None:
                visited = set()
                node = self.root
                return _in_order_recursive(node, visited)
            elif node is not None:
                _in_order_recursive(node.left, visited)
                visited.add(node)
                _in_order_recursive(node.right, visited)
            return visited

        def _in_order_iterative():
            stack, visited, node = list(), set(), self.root
            while len(stack) > 0 or node is not None:
                if node:
                    stack.append(node)
                    node = node.left
                elif len(stack) > 0: # node is None
                    node = stack.pop()
                    visited.add(node)
                    node = node.right
            return visited

        def _pre_order_recursive(node=None, visited=None):
            if visited is None:
                visited = set()
                node = self.root
                return _pre_order_recursive(node, visited)
            elif node is not None:
                visited.add(node)
                _pre_order_recursive(node.left, visited)
                _pre_order_recursive(node.right, visited)
            return visited

        def _pre_order_iterative():
            pass

        def _post_order_recursive(node=None, visited=None):
            if visited is None:
                visited = set()
                node = self.root
                return _post_order_recursive(node, visited)
            elif node is not None:
                visited.add(node)
                _post_order_recursive(node.left, visited)
                _post_order_recursive(node.right, visited)
            return visited

        def _post_order_iterative():
            pass

        #### DRIVER 
        # recursive version of the algo goes in index 1, iterative in 0
        functions = {
            'in_order': [_in_order_iterative, _in_order_recursive],
            'pre_order': [_pre_order_iterative, _pre_order_recursive],
            'post_order': [_post_order_iterative, _post_order_recursive]
        }
        # run the algorithm
        return functions[type][int(is_recursive)]()


class Vertex:
    pass


class Graph:
    def __init__(self, is_directed=False):
        pass

    def bfs(self, is_recursive=False):
        pass

    def dfs(self, is_recursive=False):
        pass
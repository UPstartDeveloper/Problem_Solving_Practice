from collections import deque


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def in_order_traversal(self, use_iteration=True):

        def _dfs_recursive(node, visited):
            if node.left is not None:
                _dfs_recursive(node.left)
            visited.add(node)
            if node.right is not None:
                _dfs_recursive(node.right)
            return visited
        
        def _dfs_iterative():
            # init collectionss
            stack = list()
            visited = set()
            # push the root onto the stack
            if self.root is not None:
                stack.append(self.root)
                # while stack !empty:  
                while len(stack) > 0:
                    # peek at the top node
                    top = stack[-1]
                    # iteratively add the unvisited left children
                    while top is not None:
                        if top.left is not None and top.left not in visited:
                            stack.append(top.left)
                        top = top.left
                    # visit the top of the stack - add to the visited set
                    if top is None and len(stack) > 0:
                        top = stack.pop()
                    visited.add(top)
                    # push the first right child onto the stack, if unvisited
                    if top.right is not None and top.right not in visited:
                        stack.append(top.right)
            # return the result
            return visited

        if use_iteration is True:
            return _dfs_iterative()
        return _dfs_recursive(self.root, set())

    def pre_order_traversal(self, use_iteration=True):
        
        def _pre_order_iterative():
            pass

        def _pre_order_recursive(node, visited):
            # visit the root of this subtree
            if node is not None:
                visited.add(node)
            # traverse the left subtree
            if node.left is not None:
                _pre_order_recursive(node.left, visited)
            # traverse the right subtree
            if node.right is not None:
                _pre_order_recursive(node.right, visited)
            return visited
            
        if use_iteration is True:
            return _pre_order_iterative()
        return _pre_order_iterative(self.root, set())

    def post_order_traversal(self, use_iteration=True):
        
        def _post_order_iterative():
            pass

        def _post_order_recursive(node, visited):
            # traverse the left subtree
            if node.left is not None:
                _post_order_recursive(node.left, visited)
            # traverse the right subtree
            if node.right is not None:
                _post_order_recursive(node.right, visited)
            # visit the root of this subtree
            if node is not None:
                visited.add(node)
            return visited
            
        if use_iteration is True:
            return _post_order_iterative()
        return _post_order_iterative(self.root, set())

    def bfs(self):
        # init collections
        q = deque()
        visited = set()
        # enqueue the first node
        if self.root is not None:
            q.append(self.root)
            while len(q) > 0:
                # dequeue a node
                node = q.popleft()
                # visit this node
                visited.add(node)
                # enqueue the neighbors
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        # return the visited nodes
        return visited

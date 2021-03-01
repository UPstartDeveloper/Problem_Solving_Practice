from collections import deque


class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def bfs(self, use_iteration=True) -> None:

        def _bfs_iterative():
            # init collections
            q = deque()
            # enqueue the root
            if self.root is not None:
                q.append(self.root)
                while len(q) > 0:
                    # dequeue the next node
                    node = q.popleft()
                    # visit it
                    print(f"Visited: {node.key}")
                    # enqueue its neighbors
                    q.extend([node.left, node.right])

        def _bfs_recursive(q=None):
            # Base Case: the queue is empty, needs to start search
            if q == None:
                q = deque()
                if self.root is not None:
                    q.append(self.root)
                return _bfs_recursive(deque())
            # Base: q is empty
            elif len(q) == 0:
                return
            # Recursive: q is not empty
            else:
                node = q.popleft()
                print(f"Visiting: {node.key}")
                q.extend([node.left, node.right])

        if use_iteration is True:
            return _bfs_iterative()
        return _bfs_recursive()

    def dfs(self, use_iteration=True, mode='in-order') -> None:

        def _dfs_iterative_in_order():
            '''due to the use of a set - time is O(n), space is O(n)'''
            # init stack
            stack = list()
            visited = set()
            # push the first node
            if self.root is not None:
                stack.append(self.root)
            # traverse the tree
            while len(stack) > 0:
                # go down as far left as possible from the top
                top = stack[-1]
                while top.left is not None and top.left not in visited:
                    stack.append(top.left)
                    top = top.left
                # visit the top
                if len(stack) > 0:
                    top = stack.pop()
                    print(f"Visiting: {top.key}")
                    visited.add(top)
                    # push the first right child
                    if top.right is not None and top.right not in visited:
                        stack.append(top.right)

        def _dfs_recursive_in_order(node=self.root):
            if node is not None: 
                if node.left is not None:
                    _dfs_recursive_in_order(node.left)
                print(f"Visiting: {node.key}")
                if node.right is not None:
                    _dfs_recursive_in_order(node.right)
        
        if use_iteration is True:
            # TODO: use a switch statement:
            pass
        # TODO: use a switch statement:
        pass

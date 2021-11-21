from collections import deque
from typing import Set


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root

    def dfs(self, method="inorder", use_iteration=True) -> Set[int]:
        ### HELPERS
        def _inorder_iterative():
            visited = set()
            node, stack = self.root, list()
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:  # stack is not empty
                    node = stack.pop()
                    visited.add(node.val)
                    node = node.right
            return visited

        def _inorder_recursive(node=self.root, visited=set()):
            if node:
                _inorder_recursive(node.left, visited)
                visited.add(node.val)
                _inorder_recursive(node.right, visited)
            return visited

        def _preorder_iterative():
            pass

        def _preorder_recursive(node=self.root, visited=set()):
            if node:
                visited.add(node.val)
                _preorder_recursive(node.left, visited)
                _preorder_recursive(node.right, visited)
            return visited

        def _postorder_iterative():
            pass

        def _postorder_recursive(node=self.root, visited=set()):
            if node:
                _postorder_recursive(node.left, visited)
                _postorder_recursive(node.right, visited)
                visited.add(node.val)
            return visited

        ### DRIVER
        functions = {
            "inorder": [_inorder_recursive, _inorder_iterative],
            "preorder": [_preorder_recursive, _preorder_iterative],
            "postorder": [_postorder_recursive, _postorder_iterative],
        }
        return functions[method][int(use_iteration)]

    def bfs(self, use_iteration=True):
        ### HELPERS
        def _bfs_iterative():
            visited = set()
            if self.root:
                q = deque([self.root])
                while q:
                    node = q.popleft()
                    visited.add(node.val)
                    for child in [node.left, node.right]:
                        if child:
                            q.append(child)
            return visited

        def _bfs_recursive(visited=set(), q=None):
            if self.root is not None and q is None:  # check for null tree
                return _bfs_recursive(visited, q=deque([self.root]))
            elif len(q) > 0:  # recursive case: continue BFS
                node = q.popleft()
                visited.add(node.val)
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
                return _bfs_recursive(visited, q)
            return visited  # base case: all done!

        ### DRIVER
        if use_iteration:
            return _bfs_iterative()
        return _bfs_recursive()

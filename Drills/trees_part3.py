from collections import deque

class TreeNode:
    def __init__(self, key: str) -> None:
        self.key = key
        self.left = self.right = None


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def bfs_iterative(self, visit: function) -> None:
        '''Assumes root is not None'''
        # A: init queue
        q = deque([self.root])
        # B: bfs the tree
        while len(q) > 0:
            node = q.popleft()
            visit(node)
            for child in [node.left, node.right]:
                if child is not None:
                    q.append(child)
        # C: {PASS} return the output of the search
        pass

    def bfs_recursive(self, visit: function, q=None) -> None:
        '''Assumes root is not None'''
        # Base Cases
        if q is None:
            # A: init queue
            q = deque([self.root])
        elif len(q) == 0:
            # C: {PASS} return output of the search
            pass
        # Recursive Case
        else:
            node = q.popleft()
            visit(node)
            for child in [node.left, node.right]:
                if child is not None:
                    q.append(child)
        
        return self.bfs_recursive(visit, q)
            
    def dfs_inorder(self, use_iteration=True) -> set:

        def _dfs_iterative(visit: function) -> None:
            # A: init stack
            if self.root is not None:
                node = self.root
                stack = list()
                # B: start the search
                while len(stack) > 0 or node is not None:
                    if node.left is not None:
                        stack.append(node)
                        node = node.left
                    else:
                        node = stack.pop()
                        visit(node)
                        node = node.right
            # C: finish the search
            return 

        def _dfs_recursive(visit: function, node=None):
            # A: init the search
            if node is None and self.root is not None:
                node = self.root
                return _dfs_recursive(visit, node)
            # B: continue the search
            elif node is not None:
                if node.left is not None:
                    _dfs_recursive(visit, node.left)
                visit(node)
                if node.right is not None:
                    _dfs_recursive(visit, node.right)
            # C: finish the search
            return

        visited = set()
        if use_iteration is True:
            return _dfs_iterative(visited.add)
        return _dfs_recursive(visited.add)



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

    def dfs(self, use_iteration=True, mode="in-order") -> None:
        def _dfs_iterative_setup():
            stack, visited = list(), set()
            if self.root is not None:
                stack.append(self.root)
            return stack, visited

        def _dfs_iterative_in_order():
            """due to the use of a set - time is O(n), space is O(n)"""
            # init collections - root is already on the stack if present
            stack, visited = _dfs_iterative_setup()
            # traverse the tree
            while len(stack) > 0:
                # go down as far left as possible from the top
                top = stack[-1]
                left_child = top.left
                while left_child is not None and left_child not in visited:
                    stack.append(left_child)
                    left_child = left_child.next
                # visit the top
                top = stack.pop()
                print(f"Visiting: {top.key}")
                visited.add(top)
                # push the first right child
                if top.right is not None and top.right not in visited:
                    stack.append(top.right)

        def _dfs_iterative_pre_order():
            """due to the use of a set - time is O(n), space is O(n)"""
            # init collections - root is already on the stack if present
            stack, visited = _dfs_iterative_setup()
            # traverse the tree
            while len(stack) > 0:
                # visit the top
                top = stack.pop()
                print(f"Visiting: {top.key}")
                visited.add(top)
                # go down as far left as possible from the top
                while top.left is not None and top.left not in visited:
                    stack.append(top.left)
                    top = top.left
                # push the first right child
                if top.right is not None and top.right not in visited:
                    stack.append(top.right)

        def _dfs_iterative_post_order():
            """due to the use of a set - time is O(n), space is O(n)"""
            # init collections - root is already on the stack if present
            stack, visited = _dfs_iterative_setup()
            # traverse the tree
            while len(stack) > 0:
                top = stack[-1]
                # go down as far left as possible from the top
                left_child = top.left
                while left_child and left_child not in visited:
                    stack.append(left_child)
                    # make sure to save a ref to the last left node pushed
                    if left_child.left:
                        left_child = left_child.left
                    else:
                        break
                # push the first right child
                right_child = top.right
                if right_child and right_child not in visited:
                    stack.append(right_child)
                # visit the top
                if left_child and left_child not in visited:
                    top = left_child
                else:  # get already visited node, or root off the stack
                    top = stack.pop()
                if top not in visited:
                    print(f"Visiting: {top.key}")
                    visited.add(top)

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

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
                    current_perm.pop(index)

            pass
        # A: init a list for the current permutation
        cp = list()
        # B: init a list to hold all the permutations
        ap = list()
        # C: exhaust all permutations
        index = 0
        backtracking_helper(cp, ap, nums)
        # D: return the permutations
        return ap

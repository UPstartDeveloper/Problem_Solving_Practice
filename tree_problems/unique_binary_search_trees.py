from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BST:
    def __init__(self, values):
        self.root = None
        for val in values:
            self.insert(val)
        
    def insert(self, val):
        """ASSUME it's ok to 'insert' values already in the tree"""
        # early exit
        if self.root is None or self.root.val == val:
            self.root = TreeNode(val)
        else:
            # make new node
            new_node = TreeNode(val)
            # find where to insert it
            parent, current_node = None, self.root
            while current_node is not None and current_node.val != val:
                parent = current_node
                if val < current_node.val:
                    current_node = current_node.left
                else:  # val > current_node.val
                    current_node = current_node.right
            # add the new node as a left or right child
            if parent.left == current_node and parent.val > val:
                parent.left = new_node
            elif parent.right == current_node and parent.val < val:
                parent.right = new_node
    
    def bfs(self):
        visited = list()
        if self.root is not None: 
            # BFS
            q = deque([self.root])
            while q:
                node = q.popleft()
                visited.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        q.append(child)
        return tuple(visited)


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Input:
            pos int
            even/odd
            node vals - 1-3
            BST- not necessarily balanced, full
            
        Output:
            int
            
        Intuition:
            permutations - 
            
        EC:
            1) n is outside the range ---> ValueError
        
        Approach:
            recursive backtracking - test all the unique structures
        
            1) Brute Force - lists
            
                n = 3   
                Permm       BFS order
                [1, 2, 3]   1, 2, 3 --> 1st
                [1, 3, 2]   1, 3, 2    2nd
                [2, 1, 3]   2, 1, 3
                [2, 3, 1]   2, 1, 3
                [3, 2, 1]   3, 2, 1
                [3, 1, 2]   3, 1, 2 --> 5th
                
                # perms (list) = # perms BST + 1
                
                for num in node_vals:
                    bst.insert(num)
                    
                A: init the node vals
                B: generate a perms of node vals (list)
                C: compute # of unique
                    1) make a BST from each perm
                    2) BFS that BST
                    3) add the output of the BFS to a set of tuples
                D: return the length of set
                    
            2) Brute force - BSTs
            
            A: init the node vals
            B: iterate over, try each val == root
            
            n = 3
            count_unique = 0  # output      choices = [1, 2, 3]      constraints
            
        
        """
        ### HELPER
        def _generate_perms(current_perm, all_perms, choices):
            # Base case: perm is done
            if len(current_perm) == n:
                all_perms.append(current_perm[:])
            # recursive: add the next value
            else:
                for index, val in enumerate(choices):
                    current_perm.append(val)
                    remaining = [
                        val for other_index, val in enumerate(choices)
                        if index != other_index
                    ]
                    _generate_perms(current_perm, all_perms, remaining)
                    current_perm.pop()
            return all_perms
        
        ### DRIVER
        # A: init the node vals
        node_vals = list(range(1, n + 1))
        # B: generate a perms of node vals (list)
        permutations = _generate_perms([], [], node_vals) 
        # C: compute # of unique
        unique_bsts = set()
        for perm in permutations:
                # 1) make a BST from each perm
                tree = BST(perm)  # TODO
                # 2) BFS that BST
                node_ordering = tree.bfs()  # TODO - return tuple(int)
                # 3) add the output of the BFS to a set of tuples
                unique_bsts.add(node_ordering)
        # D: return the length of set
        return len(unique_bsts)
 
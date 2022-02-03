from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Leetcode problem: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
        Leetcode - solution explanation: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/1687648/Python-or-Post-Order-or-Quick-easy-short
        
        Input/Problem
            binary tree, int
            >= 1
            
            good = <= distance (# of edges)
            
            distance(node1, node2) = 
                depth1 = distance from ancestor to node1
                depth2 = distance from ancestor to node2
            
        Output:
            # of good pairs
            
        Intuition:
            DFS
        
        EC:
            empty tree
            TODO
            
        Approach:
            
            BF:
                # leaf = n/2
                total = 0
                locate -> leaves = [LeafNodes] ---> # BFS
                for each leaf: # n iter
                    acculmulate total count_pairs(leaf)
                return total
                
            def count_pairs(leaf, leaves):
                for other_leaf in leaves. # n ite
                
            def find_pairs_for_one_leaf(leaf, distance):
                # A: start at root --> for each leaf
                    # save the distance to other leaves recursively
                        leafs = 0
                        pop
                        next = distance + 1
                        
                # B: DFS - count the pairs
                    # total += # left leaves * # right leaves IF <= distance
            
                
                
            
        """
        # HELPERS
        def is_leaf(node):
            return (
                node and 
                node.left is None and 
                node.right is None
            )
        
        def _init_left_right_dist_attr(node):
            node.leaf_distances = {
                "left": [],
                "right": []
            }
            
        def _dfs(visit=print):
            """iterative in-order"""
            node, stack = root, list()
            while node or len(stack) > 0:
                if node:
                    stack.append(node)
                    node = node.left
                else: 
                    node = stack.pop()
                    visit(node)
                    node = node.right
            return
            
        def _save_distances(node):
            """Makes a 'cache' or how far each node is, from all downstream leaves"""
            # Recursive: parent node
            if node and is_leaf(node) is False: 
                for child in [node.left, node.right]:
                    if child is not None:
                        _save_distances(child)
                # "inherit" the distances from the children to the leaves
                if node.left:
                    if is_leaf(node.left) is False:
                        for distances_down in node.left.leaf_distances.values():
                            node.leaf_distances["left"].extend([
                                d + 1 for d in distances_down
                            ])
                    else:  # child is a leaf, so we already know we're only 1 away
                        node.leaf_distances["left"].append(1)
                # do the same on both sides!
                if node.right:
                    if is_leaf(node.right) is False:
                        for distances_down in node.right.leaf_distances.values():
                            node.leaf_distances["right"].extend([
                                d + 1 for d in distances_down
                            ])
                    else:  # child is a leaf, so we already know we're only 1 away
                        node.leaf_distances["right"].append(1)  
                        
        def _find_good_pairs(node):
            """count how good pairs there are, for a single node"""
            count = 0
            for distance_left in node.leaf_distances["left"]:
                for distance_right in node.leaf_distances["right"]:
                    if distance_left + distance_right <= distance:
                        count += 1
            return count
                        
        def _count_good_pairs(root):
            """iterative BFS - find all pairs across the whole tree"""
            queue = q = deque([root])
            total = 0
            while len(q) > 0:
                node = q.popleft()
                total += _find_good_pairs(node)
                for child in [node.left, node.right]:
                    if child is not None:
                        q.append(child)
            return total
        
        ### MAIN
        # A: save the dist each node is to all "downstream" leaves
        _dfs(_init_left_right_dist_attr)
        _save_distances(root)
        
        # B: compute the number of good pairs - via BFS
        total = _count_good_pairs(root)
        return total

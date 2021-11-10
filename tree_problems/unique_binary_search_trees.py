class Solution:
    def __init__(self):
        self.cache = {
            0: 1,
            1: 1
        }

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
        ### DRIVER
        if n not in self.cache:
            count = 0 
            for root_node_val in range(1, n + 1):
                num_left_children = root_node_val - 0 - 1
                num_right_children = n - root_node_val
                count += (
                    self.numTrees(num_left_children) *
                    self.numTrees(num_right_children)
                )
            self.cache[n] = count
        return self.cache[n]
     

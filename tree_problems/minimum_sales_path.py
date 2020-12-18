from collections import deque

def get_cheapest_cost(rootNode):
    def get_all_paths(self, node, sum_so_far=0):
        # update the sum so far
        sum_so_far += node.cost
        # for each child in the deque
        for child_node in node.children:
            # call the function again
            get_all_paths(child_node, sum_so_far)
            # at a leaf, add the sales path
        else:
            # update the min sales path if necessary
            if sum_so_far < rootNode.min_sales_path:
                rootNode.min_sales_path = sum_so_far
        
    # get all sales paths from the root node
    min_sales_path = rootNode.get_all_paths()
    # minimum sales path
    return min_sales_path


# Time O(n), number of nodes
# Space: O(h), where h of the tree

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = deque()
        self.parent = None
        self.min_sales_path = float('inf')
        return 
   

"""
root != None

assume prices is any integer

dupes

Idea - store all sp in []
     - calculate every sp TBD
     - minimum = 
     

calculate every sp TBD

- calulate one sp

                     0 
                  /  |    \
                5    8    4
               /  \       /\
              1   2     6   8
              
              
     
rN min sp = 6
     
ssf  = 0, node = 0 [  4]

node = 4, ssf = 4, child = [6, 8]

node = 6, ssf, 10



     
     
     
     
     
     
              
 # intuition:
        - for each child
            do a DFS 
            compute the sum of each path
        - min()
 # DFS/BFS implement recurisvely
     
"""
 
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        - tree may/may not be balanced
        - at least 1 node
        - integer values for Node.val
        
        Intuition:
        
        - map each levels total sum of the node to the level itself
        
        Approach:
        # A: find the sum at each level
        # B: map that sum to the level itself
        {
            l  s
            1: 1,
            2: 7,
            3: -1
        }
             
        [1, 7, -1].index + 1
        # C: find the max sum, and return the corresponding level
        
        Edge Cases:
        - 2 levels w/ same sum? return the first
        front
          0
        [   1, 2, 3    ]
        
        
                        1
                    /       \
                   7         0 
                /   \
                7   -8
                
        q = [1]
        level = []
        level_sums = []
        
        # while until the q and level are empty
            # dequeue a node
            # "visit" # add it to the level array
                    # when the queue is empty, calculate the level sum
                    # put it in the sums array
                    enqueue all the (non-None) children of the nodes in the level array
                    remove all the nodes in level array
        """
        def get_level_sums(root):
            # A: init the level_sums array
            level_sums = list()  # O(1)
            # B: init the queue for BFS
            q = deque()  # O(1)
            level = list()  # O(1)
            # enqueue the first node
            q.append(root)  # O(1)
            # C: iterate until the queue and the level are  empty
            while not (len(q) == 0 and len(level) == 0):  # n iterations
                # dequeue a node
                node = q.popleft()  # O(1)
                # "visit" the node - add it to the level array
                level.append(node)  # O(1)
                # when the queue is empty, calculate the level sum
                if len(q) == 0:  # O(1)
                    # init the level sum
                    level_sum = 0  # O(1)
                    # enqueue all the (non-None) children 
                    index = 0  # O(1)
                    while index < len(level):  # O(log n)
                        node = level[index]  # O(1)
                        if node.left is not None:  # O(1)
                            q.append(node.left)  # O(1) 
                        if node.right is not None:  # O(1)
                            q.append(node.right)  # O(1)
                        index += 1  # O(1)
                        level_sum += node.val # O(1)
                    # empty out the level array
                    level = list()  # O(1)
                    # put the new level_sum in the sums array
                    level_sums.append(level_sum)  # O(1)
            return level_sums
        
        def get_max_level(level_sums):
            # find the max
            maximum = max(level_sums)
            # find its index
            index = level_sums.index(maximum)
            # return it (add 1)
            return index + 1
                
        # A: find the sum at each level
        # B: map that sum to the level itself
        level_sums = get_level_sums(root)  # O(n) time, O(log n) space
        # C: find the max sum, and return the corresponding level
        max_level = get_max_level(level_sums)  # O(n) time, O(1) space
        return max_level


# Time: O(n)
# Space: O(log n)
        
# Definition for a binary tree node. https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        """
        Intuition - most common elems
        
        Approach:
        Extra Space:
        1. use a dict --> 
            - rel. frequencies
            - get the highest freq
            - return [elems] of the freq
        
        2. Sorted Array
           0  1. 2. 3. 4. 5. 6
        - [5, 5, 5, 6, 6, 7, 10]
                    i
        - current_elem = 5
        _ max_occurences = 3
        - current_occurences = 3
        - modes = [(5, 3)]
        
        # A: iterate through the tree --> just find max_occurrences
        # B: iterate through the tree again --> find current_occurences, fill the array
            
        No Space:
        1. %'s? + DFS
            - modes = []
            - current_mode = 5
            - max_occurence = 0, 1, 2
            - current_elem = 5
            - current_occurences = 1, 2, 
            
        2. Top Down Recursion
        - mode of subtree = mode of left subtree and right subtree
        
        Edge Cases
        - no node -- impossible
        - imbalanced tree - long runtime
        - not an int - impossible
        
        Example:
        
                                 5
                              /     \
                              5       5  < [(6, 2), (5, 3) ]
                                       \
                                        7
                                       /   \
                                     6     10
                                      \
                                        6
                                     
        
        """
        def find_max_occurrences():
            '''iterative DFS to find how many times the modes appear'''
            # init output
            max_occurrences = 0
            current_occurrences = 0
            current_elem = root.val
            # init stack
            stack = list()
            # push first node onto stack
            node = root
            # DFS 
            while node is not None or len(stack) > 0:
                # defer the current node, go down the left subtree
                if node is not None:
                    stack.append(node)
                    node = node.left
                # visit this node
                else:
                    #  increment current_occurences
                    node = stack.pop()
                    if node.val == current_elem:
                        current_occurrences += 1
                    else:  # new node value
                        current_elem = node.val
                        current_occurrences = 1
                    # if current_occurences > max_occurences --> update the latter
                    if current_occurrences > max_occurrences:
                        max_occurrences = current_occurrences
                    # go down the right subtree
                    node = node.right
            # return the rel freq of the mode(s) in the tree
            return max_occurrences
        
        def find_modes(max_occurrences):
            '''iterative DFS to find how many times the modes appear'''
            # init output
            modes = list()
            current_occurrences = 0
            current_elem = root.val
            # init stack
            stack = list()
            # push first node onto stack
            node = root
            # DFS 
            while node is not None or len(stack) > 0:
                # defer the current node, go down the left subtree
                if node is not None:
                    stack.append(node)
                    node = node.left
                # visit this node
                else:
                    #  increment current_occurences
                    node = stack.pop()
                    if node.val == current_elem:
                        current_occurrences += 1
                    else:  # new node value
                        current_elem = node.val
                        current_occurrences = 1
                    # if current_occurences == max --> add as a mode
                    if current_occurrences == max_occurrences:
                        modes.append(current_elem)
                    # go down the right subtree
                    node = node.right
            # return the modes
            return modes
        
        
        # A: iterate through the tree --> just find max_occurrences
        max_occurrences = find_max_occurrences()
        # B: find current_occurences, fill the array
        return find_modes(max_occurrences)
        
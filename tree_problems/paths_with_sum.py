"""
Paths with Sum: 
You are given a binary tree in which each node contains an integer value 
(which might be positive or negative). 

Design an algorithm to count 
the number of paths that sum to a given value. 

The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).

Clarifying Questions:
1. is zero allowed? no
2. not a search tree? no
3. do we know anything about the tree structure:
    - balanced? no
    - full? no
    - duplicates allowed? yes
4. does the path strictly go downwards? yes
5. does a path need more than 1 node? no

Example:
   ssf = 14                 6,          value = 14 ---> 1
   c = 1                /      \        value = 0 ---> 1
                      -5         8      
                              /     \   
                             5       4
                            /
                          -5

Intuition:
- searching through all the paths (in all subtrees) to find paths
- enumerate THOSE paths
Approach:
1. Brute Force:
    # - init a count
    # - traverse through all the different paths 
    #     - find a starting node using a BFS
    #         - exhaustively DFS through all paths that start at that node
    #         - keep track of sum_so_far (ssf)
    #             - anytime we go up - remove the last added values
    #             - down - add to ssf
    #             - if ssf == value---> count +=1, go back up the tree, we're done w/ that subtree
    #             - if we hit a leaf, we're done w/ that branch, go back up
    #             - if we're done w/ all branches, go back up
    # - return the count
Edge Cases:
1. given value is 0? --> return 0 right away
2. null tree --> return 0

"""

from collections import deque


class BinaryNode:
    def __init__(self, key=None):
        self.value = key
        self.left = self.right = None


class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root = root


class Solution:
    def traverse_paths(self, node: BinaryNode, target: int) -> int:
        """
        # - anytime we go up - remove the last added values

        # down - add to ssf
        # if ssf == value---> count +=1, go back up the tree, we're done w/ that subtree
        # if we hit a leaf, we're done w/ that branch, go back up
        # if we're done w/ all branches, go back up
        """

        def pre_order_dfs(node, ssf, paths_found):
            # add the current node to the path
            if node:
                ssf += node.value
            # adding a path that meets the sum
            if ssf == target:
                paths_found += 1
            # if still < target, continue searching
            elif ssf < target: 
                # copy ssf's value, so it's not shared between branches
                ssf_on_branch = ssf
                if node.left:
                    paths_found = pre_order_dfs(node.left, ssf_on_branch, paths_found)
                if node.right:
                    # reset the sum before going right, b/c paths can only go down
                    paths_found = pre_order_dfs(node.right, ssf_on_branch, paths_found)
            # return the total number of paths
            return paths_found

        """
        # DFS
        while stack or current_node:
            if current_node:  # in in-order traversal, we go left
                stack.append(current_node)
                # ssf += current_node.value
                current_node = current_node.left
            else:  # gone all the way down the left
                current_node = stack.pop()
                # visit - increment the sum_so_far
                ssf += current_node.value
                # see if we can increment the paths
                if ssf == target:
                    paths_found += 1
                # go back up
                if current_node.left == current_node.right == None:
                    ssf += (-1 * current_node.value)
                # then, go down the right branch
                if current_node.right:
                    stack.append(current_node.right)
        """

        return pre_order_dfs(node, 0, 0)

    def paths_with_sum(self, tree: BinaryTree, target: int) -> int:
        # - init a count
        count = 0
        # validate 
        if (tree is not None and tree.root is not None and target != 0):
            # - traverse through all the different paths via BFS
            q =  deque([tree.root])
            while len(q) > 0:
                # get the node at front of the queue
                node = q.popleft()
                # "visit" DFS through all paths that start at that node
                count += self.traverse_paths(node, target)
                # enqueue the next nodes to use as a starting nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        # - return the count
        return count


if __name__ == "__main__":
    # init the tree
    node1, node2, node3, node4, node5, node6 = (
        BinaryNode(6),
        BinaryNode(-5),
        BinaryNode(8),
        BinaryNode(5),
        BinaryNode(4),
        BinaryNode(-5)
    )
    tree = BinaryTree(node1)
    node1.left = node2; node1.right = node3
    node3.left = node4; node3.right = node5
    node4.left = node6

    sol = Solution()
    print(sol.paths_with_sum(tree, 14))

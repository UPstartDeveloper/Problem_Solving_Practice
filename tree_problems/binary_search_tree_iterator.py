from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """LeetCode: https://leetcode.com/problems/binary-search-tree-iterator/"""
        # iterative, vanilla in-order DFS
        self.node, self.stack = root, list()  # last index is the top

    def next(self) -> int:
        """moves the pointer to the right, returns the value at the node"""
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        current_node = self.stack.pop()
        self.node = current_node.right
        return current_node.val

    def hasNext(self) -> bool:
        return self.node is not None or len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
"""
Assume the tree is static - structure and node values don't change

1) upfront DFS
    - return a list of all the nodes
    - iterate through the list
    - O(n) time upfront, then O(1) after --> O(1) amortized
    - O(n) space
    
2) create a min heap - slower, O(n) space
    - create a heap upfront - nlogn
    - iterate through the heap - logn
    
3) DFS-as-you-go
    - stack never exceeds O(h)
    - occasionally, finding the next node is more than O(1) - but will never exceed O(h)

"""

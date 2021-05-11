"""
Question:

Build a BST that supports the following ops:
- find()
- add_node()
- delete_node()

"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None

    def get_in_order_successor(self):
        """
           returns the child w/ the smallest value 
           in this node's right subtree

           if not there, return -1
        """
        if self.val and self.right is not None:
            successor = self.right
            while (successor.left is None and successor.right is None) is False:
                # go into the right subtree
                if successor.left:
                    successor = successor.left
                # go to the leaf in the furthest left
                elif successor.right:
                    successor = successor.right
            # return the leaf
            return successor
        # no successor
        else:
            return -1


class BST:
    def __init__(self, root: Node):
        self.root = root
        self.size = 1

    def find(self, target: int) -> int:
        '''return a Node w/ the value, or -1'''
        if self.root is not None:
            node = self.root
            while node.val != target:
                if node.val > target:
                    node = node.left
                else:  # node.val < target
                    node = node.right
            # node found
            if node is not None:
                return node
        # node not found
        return -1

    def add_node(self, value):
        '''insert the node into this tree w/ the value in sorted order'''
        # add root node
        if self.root is None:
            self.root = Node(value)
        else:  # self.root is not None
            prev, cur_node = None, self.root
            while cur_node is not None:
                # update the prev node
                prev = cur_node
                # go left 
                if value > cur_node.val:
                    cur_node = cur_node.right
                # go right
                else: # node.val <= cur_node.val
                    cur_node = cur_node.left
            # we've found a position for the new node, see where it is
            is_left_child = True
            if cur_node == prev.right:
                is_left_child = False
            # insert the new node
            if is_left_child is True:
                prev.left = Node(value)
            else:
                prev.right = Node(value)
        # increase size of tree
        self.size += 1

    def delete_node(self, value):
        """remove a node w/ this value from the tree, 
           modify the tree

           q: what to do if the node isn't present?

           no kids - it's a leaf, just make the parent's pointer None

           one kid - parent the kid to the parent of the deleted node

           two kids - promote left subtree,
                      go to the bottom of the left subtree
                      parent right subtree to the bottom of the left subtree
        """

        def delete_leaf(parent, deleted, is_left_child):
            # self.root is not being deleted
            if parent is not None:
                if is_left_child is True:
                    parent.left = None
                else:  # the deleted node is in the right subtree
                    parent.right = None
            else: # root is being deleted, and only node
                self.root = None 

        def delete_node_one_child(parent, deleted, is_left_child):
            # find the child of the deleted node
            grandchild = deleted.left
            if grandchild is None:
                grandchild = deleted.right
            # root is not being deleted
            if parent is not None and is_left_child is True:
                parent.left = grandchild
            elif parent is not None:
                parent.right = grandchild
            else:  # root is being deleted
                self.root = grandchild
     
        def delete_node_two_child(parent, deleted, is_left_child):
            '''rewrite using the in_order_successor'''
            # get the successor 
            successor = deleted.get_in_order_successor()
            # delete the node in the place of the successor - should be a leaf
            self.delete(successor.val)
            # place the val of the successor where it belongs 
            deleted.val = successor.val

        # find the node w/ the target value
        parent, deleted = None, self.root
        while deleted is not None and deleted.val != value:
            # move the parent pter
            parent = deleted
            # go left
            if value < deleted.val:
                deleted = deleted.left
            # go right
            else:  # value > deleted.right
                deleted = deleted.right
        # if value not found, raise exception
        if deleted is None:
            raise ValueError(
                f"Cannot delete node with value {value} b/c it's not present"
            )
        # value found, see which subtree that the node being deleted comes from
        is_left_child = True
        if parent is not None and parent.right == deleted:
            is_left_child = False
        # no kids - it's a leaf, just make the parent's pointer None
        if deleted.left == deleted.right == None:
            delete_leaf(parent, deleted, is_left_child)
        # one kid - parent the kid to the parent of the deleted node
        elif deleted.left is None or deleted.right is None:
            delete_node_one_child(parent, deleted, is_left_child)
        # two kids
        else: 
            delete_node_two_child(parent, deleted, is_left_child)
        # decrease tree size
        self.size -= 1
    
    def validate(self) -> bool:
        '''returns T/F based on if this BST is in sorted order'''
        if self.root is not None:
            prev, node = None, self.root
            # boiler plate DFS in order
            stack = list()
            # traverse the tree
            while node is not None or len(stack) > 0:
                # go down left subtree
                if node is not None:
                    stack.append(node)  # defer the current node
                    prev = node
                    node = node.left  
                else:  # visiting nodes
                    node = stack.pop()
                    # TODO: compare prev and node
                    if prev.val > node.val:
                        return False
                    prev = node
                    node = node.right 
        return True



    
def binary_search_iterative(array, target):
    # A: Divide - init low and high
    low, high = 0, len(array) - 1
    # B: search
    while low <= high:
        # find the middle
        mid_ndx = (low + high) // 2
        middle = array[mid_ndx]
        # found
        if middle == target:
            return mid_ndx
        # go left if the middle is too big
        elif middle > target:
            high = mid_ndx - 1 
        # go right otherwise
        else:
            low = mid_ndx + 1
    # C: not found
    return -1


def binary_search_use_recursion(array, target):
    
    def binary_search_recursive(low, high):
        # Search
        if low <= high:
            # find the middle 
            mid_ndx = (low + high) // 2
            middle = array[mid_ndx]
            # found 
            if target == middle:
                return mid_ndx
            # go left
            elif middle > target:
                return binary_search_recursive(low, mid_ndx - 1)
            # go right
            else:
                return binary_search_recursive(mid_ndx + 1, high)
        # not found
        else:
            return -1

    ############# Driver Code ###############
    return binary_search_recursive(0, len(array) - 1)


class BinaryNode:
    '''smaller than or equal items go to left, greater goes right'''
    def __init__(self, key: int):
        self.key = key
        self.left = self.right = None

    def get_inorder_successor(self):
        node = self.right
        while node and node.left:
            node = node.left
        return node
    

class BST:
    def __init__(self, root: BinaryNode):
        self.root = root

    def _find(self, item: int) -> BinaryNode:
        '''TODO: use 2 pointers'''
        parent, node = None, self.root
        while node is not None and node.key != item:
            parent = node
            if node.key <= item:
                node = node.right
            else:
                node = node.left
        return parent, node

    def search(self, integer) -> BinaryNode:
        '''Return the BinaryNode obj, or None'''
        parent, node = self._find(integer)
        return node

    def insert(self, new_item: int):
        # A: find where that new item would be located
        parent, node = self._find(new_item)
        # B: make a new node
        new_node = BinaryNode(new_item)
        # C: place the new node in the tree
        if parent is None:
            self.root = BinaryNode(new_item)
        elif new_item <= parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, item):
        # A: find the node
        # if no kids --> rm the connection from parent
        # if 1 kid --> modify parent to point to grandchild
        # if 2 kids --> find inorder successor, delete it, overwrite the node being deleted to have its value

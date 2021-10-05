##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################

# keys are unique, >= 0

# A node
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def find_largest_smaller_key(self, num):
        def dfs_in_order(node, array):
            # traverse the left subtree
            if node.left is not None:
                dfs_in_order(node.left, array)
            # visit the node - add to the array
            array.append(node.key)
            # travserse the right subtree
            if node.right is not None:
                dfs_in_order(node.right, array)
            return

        # --------
        # [5, 9, 11, 12, 14, 20, 25]
        # [14, 20, 25]
        # [14]
        # 12 < 17
        def binary_search(low, high, num):
            # calculate the middle index
            mid = (low + high) // 2
            # check the value at the middle == num and it's not the last possible value
            value = array[mid]
            # if it's num, return the left
            if value == num:
                if mid > 0:
                    return array[mid - 1]
            # if it's the last possible value return it
            elif low >= mid:
                return array[mid]
            # if value's < num
            elif value < num:
                low = mid
                # cutoff the lower half
                binary_search(low, high, num)
            # if the value's > num
            elif value >= num:
                # cutoff the higher half
                high = mid
                binary_search(low, high, num)

        # create external array
        array = list()
        # populate it with values in sorted order
        dfs_in_order(self.root, array)
        # binary search for the element largest smaller
        return binary_search(0, len(array) - 1, num)

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while currentNode is not None:
            if key < currentNode.key:
                if currentNode.left is None:
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
            else:
                currentNode = currentNode.left
                if currentNode.right is None:
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right


#########################################
# Driver program to test above function #
#########################################

bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(17)

print("Largest smaller number is %d " % (result))


"""
Binary Search Idea

Scenario:
- if num is a Key
- binary search for it
- return it's left child, or the parent (or -1 if it's a leaf)
- if num is not a key

"""

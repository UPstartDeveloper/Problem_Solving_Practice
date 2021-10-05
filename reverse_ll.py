### do not modify this class
class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


### do not modify this class, or any of the methods in it, other than reverse()
### you may insert new methods if you like
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node

    def extend(self, array):
        for element in array:
            self.append(element)

    # used in test cases verify correct solutions
    # if you want to test your code without submitting, consider using this function
    def to_array(self):
        array = []
        curr = self.head
        while curr != None:
            array.append(curr.data)
            curr = curr.next
        return array

    # implement this method
    def reverse(self):
        def reverse_iterative():
            # init a stack - LIFO
            # bottom of stack - 0 index
            # top of top --> last index
            stack = list()
            # iterate from head to tail, push each onto the stack
            node = self.head
            while node is not None:
                # push onto the stack
                stack.append(node)
                # move on to the next node
                node = node.next
            # set the head to be the top of the stack
            self.head = stack.pop(-1)
            # reverse the LL
            node = self.head
            # [1]. 2 -> 1
            while len(stack) > 0:
                # pop each off node
                next_node = stack.pop(-1)
                # reassign the next pointers
                node.next = next_node
                # move the node to the next_node in the list
                node = next_node
            # reassign the tail
            self.tail = node
            self.tail.next = None
            return None

        def reverse_recursive(prev_node, node):
            # Base Case
            if node is None:
                return node
            # Recursive Case - pushing onto the stack
            if node is not None and node.next is not None:
                return reverse_recursive(node.next)
            # Recursive Case - pop off the stack
            elif node is not None:
                self.head = node
                reverse_recursive(self.head)
                # node.next = reverse_recursive(node.next)

        """
                     bottom         top
        call stack = 1 -> 2->
        prev_node  |   node | 
        """

        # return reverse_iterative()
        node = self.head
        reverse_recursive(node)


"""
  LL: 1->2->3->4->5->NULL
      H           T
  LL: 5->4->3->2->1->NULL
          bottom.        top
  stack = []
  
  node = 1
  next_node = 1
"""

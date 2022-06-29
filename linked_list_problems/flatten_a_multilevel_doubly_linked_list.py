class Node:
    # Definition for a Node.
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        """
        You are given a doubly linked list, which contains nodes that have a 
            next pointer, 
            a previous pointer, and an additional 
            child pointer. 
                may or may not point to a separate doubly linked list, 
                also containing these special nodes.
                
        These child lists may have one or more children of their own, and so on, 
        to produce a multilevel data structure as shown in the example below.

        Given the head of the first level of the list, 
        flatten the list so that all the nodes appear in a single-level, 
            doubly linked list. 
        
        What's the order gonna be?
            Let curr be a node with a child list. 
            The nodes in the child list should appear after curr and before curr.next 
            in the flattened list 

            (backtracking???)

        Output:
            Return the head of the flattened list. 
            The nodes in the list must have all of their child pointers set to null.

        Intuition:
            recursive backtracking
            divide and conqer

        EC:
            # nodes > 1000 ---> ValuError
            invalid node vals --> ValueError
            null head --> return None

        Approach:

            Stepping Stones:

            1) merge a single node into parent list:
                temp = 3.next
                3.next = 3.child
                temp.prev = 3.next

            2) merge a list into parent list
                
                A: init node runner @ head

                B: traverse DLL - go to the tail, don't go over

                    1) check if node.child:
                        temp = node.next
                        node.next = node.child
                        temp.prev = _recurse(child list, aka node.child)
                        node.child = None
                        node = temp
                    2) else if node.next:
                        node = node.next

                C: return node

        """
        ### HELPERS
        def _traverse(node):
            """recursive traversal algo"""
            # A:
            while node:
                # B: the "merge" operation
                if node.child:
                    temp = node.next
                    node.next = node.child
                    node.child.prev = node
                    # divide - traverse in a separate stack frame
                    child_list_tail = _traverse(node.child)
                    # conquer - connect the nodes in 1 line
                    child_list_tail.next = temp
                    if temp:
                        temp.prev = child_list_tail
                    # move forward
                    node.child = None
                    node = temp
                elif node.next is not None:
                    node = node.next
                else:  # avoid infinite loop
                    break
            # C: return tail
            return node

        ### EC
        if not head:
            return None

        ### DRIVER
        final = _traverse(head)  # helper
        final.next = None
        return head


"""
                                                n
 1---2---3--7---8--11--12--9---10--4---5---6--NULL
         |
                            n
         7---8--11--12--9---10--NULL
             |
                  n
             11--12--NULL

"""

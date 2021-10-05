# Problem Description from Leetcode: https://leetcode.com/problems/design-circular-queue/


class DoublyLinkedNode:
    def __init__(self, val, next_node=None, prev=None):
        self.val = val
        self.next_node = self.prev = None


class DoublyLinkedList:
    def __init__(self, is_circular):
        self.head, self.tail = (DoublyLinkedNode(-1), DoublyLinkedNode(-1))
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        # make circular
        if is_circular:
            self.tail.next = self.head

    def append(self, node: DoublyLinkedNode):
        # make the new node point .next to the tail
        node.next = self.tail
        # make it also point to the old_tail_before as prev
        node.prev = self.tail.prev
        # make the old_tail_before.next to the next node
        self.tail.prev.next = node
        # make the self.tail.prev --> new node
        self.tail.prev = node
        # increment size
        self.size += 1

    def pop_head(self) -> DoublyLinkedNode:
        if self.size > 0:
            # save node that's currently after the head
            first = self.head.next
            # make the self.head.next ---> old_head_after.next
            self.head.next = first.next
            # make old_head_after.next.prev --> self.head
            first.next.prev = self.head
            # decrement size
            self.size -= 1
            return first
        return None

    def get_head(self) -> int:
        """assumes a node is after self.head"""
        return self.head.next.val

    def get_tail(self) -> int:
        """assumes a node is before self.tail"""
        return self.tail.prev.val

    def is_empty(self) -> bool:
        return self.size == 0


class MyCircularQueue:
    """
    Intution:

        head node ---> front of queue
        tail node ---> back of the queue

    """

    def __init__(self, k: int):
        # make a list, and self.k
        self.queue = DoublyLinkedList(is_circular=True)
        self.size_limit = k

    def enQueue(self, value: int) -> bool:
        """check curreent size againsrt hte k"""
        if self.isFull() is False:
            # add a new node to the end of the list
            self.queue.append(DoublyLinkedNode(value))
            return True
        return False

    def deQueue(self) -> bool:
        """"""
        # check if not empty
        if self.isEmpty() is False:
            # pop from the end of the list - list.pop()
            self.queue.pop_head()
            return True
        return False  # could not dequeue

    def Front(self) -> int:
        if self.isEmpty() is False:
            return self.queue.get_head()
        return -1

    def Rear(self) -> int:
        if self.isEmpty() is False:
            return self.queue.get_tail()
        return -1

    def isEmpty(self) -> bool:
        return self.queue.size == 0

    def isFull(self) -> bool:
        return self.queue.size == self.size_limit


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

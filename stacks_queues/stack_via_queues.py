class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        LeetCode: https://leetcode.com/problems/implement-stack-using-queues/
        """
        self.q1 = list()
        self.q2 = list()

    def _find_last_enqueued(self, delete):
        # dequeue all but back of q1, onto q2
        for index in range(len(self.q1) - 1):
            item = self.q1[index]
            self.q2.append(item)
        # switch the pointers
        self.q1, self.q2 = self.q2, [self.q1[-1]]
        # copy/delete the value left
        last = self.q2.pop()
        if delete is False:
            self.q1.append(last)
        return last

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.q1) == 1:
            return self.q1.pop()

        elif len(self.q1) > 1:
            last = self._find_last_enqueued(True)
            return last

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.q1) == 1:
            return self.q1[0]

        elif len(self.q1) > 1:
            return self._find_last_enqueued(False)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

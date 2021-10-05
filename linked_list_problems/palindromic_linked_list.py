# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    # ------ Helpers --------------
    def find_middle_and_end(head):
        # A: init two pointers
        slow, fast = head, head.next
        # B: iterate until one's at middle, other near the end
        while fast.next:
            slow = slow.next
            # for odd number of nodes, move fast ahead just by 1 at the end
            if fast.next.next is not None:
                fast = fast.next.next
            elif fast.next is not None:  # we only need to move forward 1 more
                fast = fast.next
        # C: return the pointers
        return slow, fast

    def reverse_last_half(middle, last):
        if middle.next != last:
            # copy the next node from the middle (slow pointer)
            temp = middle.next
            if temp.next == last:
                temp.next = None
            # make the next node from the middle the last, and re-insert prev
            middle.next = last
            last.next = temp
            # move forward middle and last nodes
            middle = middle.next
            last = last.next
            print(last.val, last.next)
            # start reversing, while last node is not the tail
            while last.next is not None:
                print("in loop")
                # reset last node after the middle
                last = middle.next
                # take the node after the last node for next pointer swap
                temp = last.next
                middle.next = temp
                temp.next = last
                # move forward middle and last nodes
                middle = middle.next
                last = last.next

    def check_palindrome(middle) -> bool:
        node = head
        # ignore nodes smack right in the middle
        middle = middle.next
        # check nodes in each corresponding position in 1st and 2nd halves
        while middle is not None:
            # fail fast
            if node.val != middle.val:
                # print(node, middle)
                return False
            # move forward
            node = node.next
            middle = middle.next
        return True

    # ------ Driver --------------
    if not head or not head.next:
        return True
    # A: find the middle and end of the LL
    middle, last = find_middle_and_end(head)
    print("found middle", middle.val)
    # B: reverse the second half of the LL
    reverse_last_half(middle, last)
    print("reversed list")
    # C: find the middle again
    middle, last = find_middle_and_end(head)
    # D: check that the list is a palindrome
    return check_palindrome(middle)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)

    print(isPalindrome(head))

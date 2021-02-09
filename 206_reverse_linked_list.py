# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head

        while current is not None:
            tmp = current
            current = current.next
            tmp.next = previous
            previous = tmp

        return previous

    def recursiveReverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        next_node = self.recursiveReverseList(head.next)
        head.next.next = head
        head.next = None
        return next_node


if __name__ == '__main__':
    # begin
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode())))))

    answer = s.recursiveReverseList(head)
    while answer is not None:
        print(answer.val)
        answer = answer.next

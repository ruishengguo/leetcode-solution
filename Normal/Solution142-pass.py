# 142、环形链表 II
from setup import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        while True:
            if not head:
                break
            if head in nodes:
                return head
            else:
                nodes.add(head)
                head = head.next

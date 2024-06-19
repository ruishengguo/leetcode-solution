# 19、删除链表的第N个节点
from setup import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = [head]
        cur = head
        while cur:
            cur = cur.next
            nodes.append(cur)
        l = len(nodes)
        if l == 2:
            return None
        elif n == l - 1:
            return nodes[1]
        nodes[-n-2].next = nodes[-n-1].next
        return nodes[0]

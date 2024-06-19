# 203、移除链表元素
from typing import Optional
from setup import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            return ListNode(head.val, self.removeElements(head.next, val))

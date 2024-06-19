# 206、反转链表
from typing import Optional

from setup import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(root: Optional[ListNode], inter: Optional[ListNode]) -> Optional[ListNode]:
            if not root:
                return inter
            return rev(root.next, ListNode(root.val, inter))

        return rev(head, None)
    
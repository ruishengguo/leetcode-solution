# 234、回文链表
from typing import Optional

from setup import ListNode, CreateMethods


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(root: Optional[ListNode], other: Optional[ListNode]) -> Optional[ListNode]:
            if root is None:
                return other
            return reverse(root.next, ListNode(root.val, other))

        new = None
        new = reverse(head, new)

        def is_one(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
            if l1 is None:
                return True
            if l1.val == l2.val:
                return is_one(l1.next, l2.next)
            else:
                return False

        return is_one(new, head)

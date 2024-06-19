# 合并两个有序链表

from typing import Optional
from setup import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list2 = ListNode(val=list1.val, next=list2)
            return self.mergeTwoLists(list1.next, list2)
        else:
            return ListNode(val=list2.val, next=self.mergeTwoLists(list1, list2.next))

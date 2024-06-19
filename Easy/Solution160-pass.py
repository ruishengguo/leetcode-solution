# 160、相交链表
from setup import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = set()
        while headA:
            l1.add(headA)
            headA = headA.next
        while headB:
            if headB in l1:
                return headB
            headB = headB.next

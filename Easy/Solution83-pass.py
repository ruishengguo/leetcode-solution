# 83、删除排序链表中的重复元素

from setup import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        in_it = []

        def func(l_n):
            if l_n is None:
                return None
            elif l_n.val in in_it:
                return func(l_n.next)
            else:
                in_it.append(l_n.val)
                return ListNode(val=l_n.val, next=func(l_n.next))

        return func(head)

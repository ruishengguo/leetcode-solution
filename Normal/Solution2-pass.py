# 2、两数之和
from setup import ListNode, CreateMethods, GetMethods


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        else:
            if not l2:
                l2 = ListNode()
            l2.val += l1.val
            if l2.val >= 10:
                time = l2.val // 10
                l2.val -= 10 * time
                if not l1.next:
                    l1.next = ListNode(0)
                l1.next.val += time
            return ListNode(val=l2.val, next=self.addTwoNumbers(l1.next, l2.next))


s = Solution()
print(GetMethods.get_list(s.addTwoNumbers(CreateMethods.new_ListNode([9, 9, 9, 9]),
                                          CreateMethods.new_ListNode([9, 9, 9, 9, 9, 9, 9]))))

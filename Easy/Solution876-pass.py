# 876、链表的中间结点
from setup import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def get_depth(root):
            if root:
                return 1 + get_depth(root.next)
            return 0

        d = get_depth(head) // 2

        def depth_get_list(root, depth_remain):
            if depth_remain != 0:
                return depth_get_list(root.next, depth_remain - 1)
            return root

        return depth_get_list(head, d)

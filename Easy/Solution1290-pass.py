# 1290、二进制链表转整数
from setup import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        res = 0
        while cur:
            res *= 2
            res += cur.val
            cur = cur.next
        return res

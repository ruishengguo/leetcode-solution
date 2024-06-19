# 141、环形链表
from typing import Optional
from setup import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        loc = set()
        rt = head
        while rt:
            if rt in loc:
                return True
            loc.add(rt)
            rt = rt.next
        return False

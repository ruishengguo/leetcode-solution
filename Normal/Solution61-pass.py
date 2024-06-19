from typing import Optional, List, Tuple

from Normal.setup import ListNode


class Solution:
    def count(self, head: Optional[ListNode]) -> Tuple[List[Optional[ListNode]], int]:
        result = 1
        nodes = [head]
        cur = head
        while cur.next:
            result += 1
            cur = cur.next
            nodes.append(cur)
        cur.next = head
        return nodes, result

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        lst, num = self.count(head)
        k %= num
        lk = (k + 1) % num
        ret = lst[-k]
        last = lst[-lk]
        last.next = None
        return ret

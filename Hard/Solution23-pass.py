# 23、合并K个升序链表
from typing import Optional, List
from setup import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new = []
        while True:
            min_ = [10001, []]
            for index, i in enumerate(lists):
                if not i:
                    continue
                if i.val < min_[0]:
                    min_ = [i.val, [index]]
                elif i.val == min_[0]:
                    min_[1].append(index)
            if not min_[1]:
                new.append(None)
                break
            for i in min_[1]:
                node, lists[i] = lists[i], lists[i].next
                node.next = None
                new.append(node)
        for index in range(len(new) - 1):
            new[index].next = new[index + 1]
        return new[0]

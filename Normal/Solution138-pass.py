# 138、复制带随机指针的链表
from typing import Optional
from setup.Node import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = []
        new_nodes = []
        rand = []

        def get_list(h):
            if not h:
                nodes.append(None)
                return
            nodes.append(h)
            get_list(h.next)

        get_list(head)
        for i in nodes[:-1]:
            new_nodes.append(Node(i.val))
        new_nodes.append(None)
        for i in nodes[:-1]:
            rand.append(nodes.index(i.random))
        for i in range(len(new_nodes) - 1):
            new_nodes[i].next = new_nodes[i + 1]
            new_nodes[i].random = new_nodes[rand[i]]
        del get_list, i, rand
        return new_nodes[0]

# 707、设计链表
from setup import ListNode


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.end = self.head
        else:
            new_head = ListNode(val)
            new_head.next = self.head
            self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.end = self.head
        else:
            self.end.next = ListNode(val)
            self.end = self.end.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index <= 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            slow = self.head
            fast = self.head.next
            new = ListNode(val)
            for i in range(index - 1):
                slow = fast
                fast = fast.next
            slow.next = new
            new.next = fast
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            if index == self.length - 1:
                self.end = cur
        self.length -= 1

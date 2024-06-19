from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class CreateMethods:
    @staticmethod
    def new_ListNode(lst: Optional[List[int]]) -> Optional[ListNode]:
        if not lst:
            return None
        elif len(lst) > 1:
            return ListNode(lst[0], CreateMethods.new_ListNode(lst[1:]))
        else:
            return ListNode(lst[0])


class GetMethods:
    @staticmethod
    def get_list(lst: Optional[ListNode]) -> Optional[List]:
        if not lst:
            return None
        elif lst.next:
            res = [lst.val]
            res.extend(GetMethods.get_list(lst.next))
            return res
        else:
            return [lst.val]


class Codec:
    @staticmethod
    def serialize(root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        pile = [root]
        while True:
            new_pile = []
            end = True
            for i in pile:
                if isinstance(i, TreeNode):
                    res.append(i.val)
                    new_pile += [i.left, i.right]
                    end = False
                else:
                    res.append(None)
            if end:
                break
            pile = new_pile[:]
        while True:
            node = res.pop()
            if node is not None:
                res.append(node)
                break
        return str(res)

    @staticmethod
    def deserialize(data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = list(map(lambda x: int(x) if x != 'None' and x != 'null' else None, ''.join(data[1:-1].split(' ')).split(',')))[::-1]
        pile = [TreeNode(data.pop())]
        cur = 0
        while data:
            l = data.pop()
            if data:
                r = data.pop()
            else:
                r = None
            if l is not None:
                l = TreeNode(l)
                pile.append(l)
            if r is not None:
                r = TreeNode(r)
                pile.append(r)
            pile[cur].left, pile[cur].right = l, r
            cur += 1
        return pile[0]

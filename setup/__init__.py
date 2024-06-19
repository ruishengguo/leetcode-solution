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


class CreateMethods:
    @staticmethod
    def new_ListNode(lst: Optional[List[int]]) -> Optional[ListNode]:
        if not lst:
            return None
        elif len(lst) > 1:
            return ListNode(lst[0], CreateMethods.new_ListNode(lst[1:]))
        else:
            return ListNode(lst[0])

    @staticmethod
    def new_TreeNode(lst: Optional[List]) -> Optional[TreeNode]:
        if not lst:
            return None
        if isinstance(lst[1], List):
            new = TreeNode(lst[0], CreateMethods.new_TreeNode(lst[1]))
        elif isinstance(lst[1], int):
            new = TreeNode(lst[0], TreeNode(lst[1]))
        else:
            new = TreeNode(lst[0])
        if isinstance(lst[2], List):
            new.right = CreateMethods.new_TreeNode(lst[2])
            return new
        elif isinstance(lst[2], int):
            new.right = TreeNode(lst[2])
            return new
        else:
            return new


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

    @staticmethod
    def get_tree(tree: Optional[TreeNode]) -> Optional[List]:
        if not tree:
            return None
        left = GetMethods.get_tree(tree.left)
        right = GetMethods.get_tree(tree.right)
        return [tree.val, left, right]

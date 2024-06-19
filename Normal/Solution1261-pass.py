# 1261、在受污染的二叉树中查找元素
from typing import Optional
from setup import TreeNode


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.has = set()
        if not root:
            return
        else:
            root.val = 0
            self._get_all(root)

    def _get_all(self, root: Optional[TreeNode]):
        if not root:
            return
        self.has.add(root.val)
        if root.left:
            root.left.val = root.val * 2 + 1
            self._get_all(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            print(root.right.val)
            self._get_all(root.right)

    def find(self, target: int) -> bool:
        return target in self.has

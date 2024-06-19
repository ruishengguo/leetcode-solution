# 剑指 Offer II 055、二叉搜索树迭代器
from typing import Optional, List
from setup import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.tree = self.inorderTraversal(root)
        self.cur = 0
        self.max_ = len(self.tree)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        all_ = []
        if root.left is not None:
            all_.extend(self.inorderTraversal(root.left))
        all_.append(root.val)
        if root.right is not None:
            all_.extend(self.inorderTraversal(root.right))
        return all_

    def next(self) -> int:
        res = self.tree[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return self.cur < self.max_

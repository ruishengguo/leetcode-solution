# 面试题 04.06、后继者
from typing import Optional, List
from setup import TreeNode


class Solution:
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

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        t = self.inorderTraversal(root) + [None]
        i = t.index(p.val)
        ret = TreeNode(t[i + 1])
        return ret if ret.val else None

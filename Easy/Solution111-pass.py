# 111、二叉树的最小深度
from setup import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        for i in (root.left, root.right):
            if not i:
                continue
            if not (i.left or i.right):
                return 2
        nxt = []
        if root.left:
            nxt.append(self.minDepth(root.left))
        if root.right:
            nxt.append(self.minDepth(root.right))
        return min(nxt) + 1

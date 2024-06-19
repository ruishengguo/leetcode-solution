# 1022、从根到叶的二进制数之和
from typing import Optional
from setup import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not (root.left or root.right):
            return root.val
        res = 0
        root.val *= 2
        if root.left:
            root.left.val += root.val
            res += self.sumRootToLeaf(root.left)
        if root.right:
            root.right.val += root.val
            res += self.sumRootToLeaf(root.right)
        return res

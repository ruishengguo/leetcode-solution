# 2236、判断根结点是否等于子结点之和
from typing import Optional
from setup import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

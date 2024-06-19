# 112、路径总和
from typing import Optional
from setup import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        else:
            nxt = targetSum - root.val
            return self.hasPathSum(root.left, nxt) or self.hasPathSum(root.right, nxt)

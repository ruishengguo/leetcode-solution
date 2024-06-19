# 1305、两棵二叉搜索树中的所有元素
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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return sorted(self.inorderTraversal(root1) + self.inorderTraversal(root2))

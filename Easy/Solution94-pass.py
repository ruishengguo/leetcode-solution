# 94、二叉树的中序遍历


# Definition for a binary tree node.
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

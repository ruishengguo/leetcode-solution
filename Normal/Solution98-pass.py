# 98、验证二叉搜索树
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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        r = self.inorderTraversal(root)
        temp = r[0]
        for i in r[1:]:
            if i <= temp:
                return False
            temp = i
        return True

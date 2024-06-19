# 450、删除二叉搜索树中的节点
from typing import Optional, List
from setup import TreeNode


class Solution:
    def convertBiNode(self, lst: List[int]) -> TreeNode:
        ret = TreeNode()
        cur = ret
        for n in lst:
            cur.right = TreeNode(n)
            cur = cur.right
        return ret.right

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

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        lst = self.inorderTraversal(root)
        if key in lst:
            lst.remove(key)
            return self.convertBiNode(lst)
        return root

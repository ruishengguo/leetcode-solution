# 257、二叉树的所有路径
from typing import Optional, List
from setup import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> Optional[List[str]]:
        if not root:
            return None
        if not (root.left or root.right):
            return [str(root.val)]
        else:
            res = []
            lt = self.binaryTreePaths(root.left)
            rt = self.binaryTreePaths(root.right)
            if not lt:
                lt = []
            elif not rt:
                rt = []
            lt.extend(rt)
            for i in lt:
                res.append(str(root.val) + '->' + i)
            return res

# 101、对称二叉树

from setup import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None or root.right is None:
            if root.left is not None or root.right is not None:
                return False
            else:
                return True
        else:
            if root.left.val == root.right.val:
                return self.isSymmetric(TreeNode(left=root.left.left, right=root.right.right)) and \
                       self.isSymmetric(TreeNode(left=root.left.right, right=root.right.left))
            else:
                return False

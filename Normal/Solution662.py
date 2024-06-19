# 662、二叉树最大宽度

from typing import Optional
from setup import TreeNode, CreateMethods, GetMethods


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]):
        widths = {0: [1, True]}

        def fill_widths(rt: Optional[TreeNode], depth=0):
            addition = 0
            do_it = False
            if isinstance(rt.left, TreeNode) and (rt.left.left is not None or rt.left.right is not None):
                addition += 2

                fill_widths(rt.left, depth + 1)
                if rt.left.left is not None or rt.left.right is not None:
                    do_it = True
            if isinstance(rt.right, TreeNode) and (rt.right.left is not None or rt.right.right is not None):
                addition += 2
                fill_widths(rt.right, depth + 1)
                if rt.right.left is not None or rt.right.right is not None:
                    do_it = True
            if addition != 0:
                try:
                    widths[depth + 2][0] += addition
                except KeyError:
                    widths[depth + 2] = [addition, False]
                if do_it:
                    widths[depth + 2][1] = True

        fill_widths(TreeNode(left=root, right=None), -1)
        result = []
        for key in widths:
            if widths[key][1]:
                result.append(widths[key][0])
        return max(result)


s = Solution()
# print(s.widthOfBinaryTree(TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5)), right=TreeNode(val=2))))
# print(s.widthOfBinaryTree(TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5), right=TreeNode(val=3)), right=None)))
# print(s.widthOfBinaryTree(TreeNode(val=1, left=TreeNode(val=3, left=TreeNode(val=5, left=None, right=None),
#                                                         right=TreeNode(val=3, left=None, right=None)),
#                                    right=TreeNode(val=2, left=None, right=TreeNode(val=9, left=None, right=None)))))

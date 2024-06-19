# 100、相同的树

from setup import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            if p is not None or q is not None:
                return False
            else:
                return True
        if p.val != q.val:
            return False
        else:
            for i in [(p.left, q.left), (p.right, q.right)]:
                if i[0] is not None:
                    if i[1] is None:
                        return False
                    else:
                        if not self.isSameTree(i[0], i[1]):
                            return False
                else:
                    if i[1] is not None:
                        return False
        return True


s = Solution()
print(s.isSameTree(None, TreeNode()))

from typing import Optional, List

from setup import TreeNode, CreateMethods, GetMethods


class Solution:
    def is_same_tree(self, p, q):
        if not p:
            return not q
        if not q:
            return not p
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        my_hash = {}
        res = []

        def f(root1):
            if root1.left:
                bp = False
                for key in my_hash:
                    if self.is_same_tree(root1.left, key[0]):
                        my_hash[key] += 1
                        bp = True
                        break
                if not bp:
                    my_hash[(root1.left, None)] = 1
                f(root1.left)
            if root1.right:
                bp = False
                for key in my_hash:
                    if self.is_same_tree(root1.right, key[0]):
                        my_hash[key] += 1
                        bp = True
                        break
                if not bp:
                    my_hash[(root1.right, None)] = 1
                f(root1.right)

        f(root)
        for key_ in my_hash:
            if my_hash[key_] > 1:
                res.append(key_[0])
        return res


s = Solution()
r = s.findDuplicateSubtrees(CreateMethods.new_TreeNode([1, [2, [4, None, None], None],
                                                       [3, [2, [4, None, None], None], 4]]))
for i in r:
    print(GetMethods.get_tree(i))


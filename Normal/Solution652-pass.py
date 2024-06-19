# 652、寻找重复的子树
from typing import Optional, List
from setup import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p or q):
            return True
        elif not (p and q):
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root or not(root.right or root.left):
            return []
        elif not(root.right and root.left):
            return self.findDuplicateSubtrees(root.left if root.left else root.right)
        root_same = {}

        def DFS(rt):
            if not rt:
                return
            else:
                if rt.val not in root_same:
                    root_same[rt.val] = [rt]
                else:
                    root_same[rt.val].append(rt)
                DFS(rt.left)
                DFS(rt.right)

        DFS(root.left)
        DFS(root.right)
        res = []
        pops = []
        for i in root_same:
            if len(root_same[i]) == 1:
                pops.append(i)
        for i in pops:
            root_same.pop(i)
        for i in root_same:
            roots = {}
            for j in root_same[i]:
                have = False
                for k in roots:
                    if self.isSameTree(j, k):
                        have = True
                        roots[k] += 1
                        break
                if not have:
                    roots[j] = 1
            for j in roots:
                if roots[j] != 1:
                    res.append(j)
        return res


s = Solution()
print(s.findDuplicateSubtrees(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4)))))

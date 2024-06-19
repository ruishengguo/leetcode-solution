# 987、二叉树的垂序遍历
from typing import Optional, List

from setup import TreeNode


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        buckets = {}

        def Traversal(rt: Optional[TreeNode], posx: int, depth: int) -> None:
            if not rt:
                return
            if posx not in buckets:
                buckets[posx] = {depth: [rt.val]}
            elif depth not in buckets[posx]:
                buckets[posx][depth] = [rt.val]
            else:
                buckets[posx][depth].append(rt.val)

            Traversal(rt.left, posx - 1, depth + 1)
            Traversal(rt.right, posx + 1, depth + 1)

        Traversal(root, 0, 0)
        res = []
        external_key = []
        for i in buckets:
            key = []
            item = []
            for j in buckets[i]:
                key.append(j)
            for j in sorted(key):
                item += sorted(buckets[i][j])
            buckets[i] = item
            external_key.append(i)
        for i in sorted(external_key):
            res.append(buckets[i])
        return res

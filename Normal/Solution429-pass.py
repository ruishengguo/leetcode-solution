# 429、N 叉树的层序遍历
from setup import Node
from typing import List


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        res = []
        if not root:
            return res

        def level_(rt: Node, depth=0):
            if len(res) == depth:
                res.append([])
            res[depth].append(rt.val)
            for i in rt.children:
                level_(i, depth + 1)

        level_(root)
        return res

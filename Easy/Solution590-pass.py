# 590、N 叉树的后序遍历
from typing import List
from setup import Node


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        for i in map(lambda x: self.postorder(x), root.children):
            res += i
        res.append(root.val)
        return res

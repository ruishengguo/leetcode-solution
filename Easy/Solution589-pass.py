# 589、N 叉树的前序遍历
from typing import List
from setup import Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = [root.val]
        for i in map(lambda x: self.preorder(x), root.children):
            res += i
        return res

# 559、N叉树的最大深度
from setup import Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        else:
            return 1 + max(map(lambda x: self.maxDepth(x), root.children))

# 面试题 17.12、BiNode
from typing import Optional, List

from setup import TreeNode, Codec


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        all_ = []
        if root.left is not None:
            all_.extend(self.inorderTraversal(root.left))
        all_.append(root.val)
        if root.right is not None:
            all_.extend(self.inorderTraversal(root.right))
        return all_

    def nodeGenerator(self, root: TreeNode):
        lst = self.inorderTraversal(root)
        lst.append(None)
        index = 0
        while True:
            yield lst[index]
            index += 1

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        g = self.nodeGenerator(root)
        ret = TreeNode()
        cur = ret
        while True:
            n = next(g)
            if n is None:
                return ret.right
            else:
                cur.right = TreeNode(n)
                cur = cur.right


s = Solution()
print(Codec.serialize(s.convertBiNode(Codec.deserialize('[4,2,5,1,3,null,6,0]'))))

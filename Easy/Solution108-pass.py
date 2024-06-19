# 108、将有序数组转换为二叉搜索树
from typing import List, Optional
from setup import TreeNode, GetMethods


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 2:
            return TreeNode(val=nums[1], left=TreeNode(nums[0]))
        elif length == 1:
            return TreeNode(nums[0])
        else:
            return TreeNode(val=nums[length // 2], left=self.sortedArrayToBST(nums[:length // 2]),
                            right=self.sortedArrayToBST(nums[length // 2 + 1:]))

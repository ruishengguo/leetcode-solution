# 2154、将找到的值乘以二
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original in nums:
            return self.findFinalValue(nums, original * 2)
        else:
            return original

# 1920、基于排列构建数组
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(nums[i])
        return res

# 268、丢失的数字
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            res ^= i
        for i in nums:
            res ^= i
        return res

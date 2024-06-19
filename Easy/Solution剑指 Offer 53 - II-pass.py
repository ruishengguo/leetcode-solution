# 剑指 Offer 53 - II、0～n-1中缺失的数字
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.extend(list(range(nums[0], len(nums) + 1)))
        res = 0
        for i in nums:
            res ^= i
        return res

# 462、最少移动次数使数组元素相等 II
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        medium = nums[len(nums) // 2]
        res = 0
        for i in nums:
            res += abs(medium - i)
        return res

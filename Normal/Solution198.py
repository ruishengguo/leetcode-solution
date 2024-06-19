# 198、打家劫舍
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        elif l == 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in nums[2:]:
            dp.append(max(dp[-2] + i, dp[-1]))
        return dp[-1]

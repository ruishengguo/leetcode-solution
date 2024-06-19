# 713、乘积小于 K 的子数组
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res, initial, i = 0, 1, 0
        for j, num in enumerate(nums):
            initial *= num
            while initial >= k and i <= j:
                initial //= nums[i]
                i += 1
            res += j - i + 1
        return res

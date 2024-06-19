# 908、最小差值
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        delta = max(nums) - min(nums)
        maximum = k * 2
        if delta <= maximum:
            return 0
        else:
            return delta - maximum

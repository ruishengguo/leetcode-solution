# 1979、找出数组的最大公约数
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s, l = min(nums), max(nums)
        while l % s != 0:
            l, s = s, l % s
        return s

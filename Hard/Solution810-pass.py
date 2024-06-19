# 810、黑板异或游戏
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        else:
            res = 0
            for i in nums:
                res ^= i
            return res == 0

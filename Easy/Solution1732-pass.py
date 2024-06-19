# 1732、找到最高海拔
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        max_ = 0
        for i in range(len(gain) - 1):
            gain[i + 1] = gain[i] + gain[i + 1]
            max_ = max(max_, gain[i + 1])
        return max_

# 1014、最佳观光组合
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dpi = values[0] + 0
        max_ = 0
        for j in range(1, len(values)):
            max_ = max(max_, dpi + values[j] - j)
            dpi = max(dpi, values[j] + j)
        return max_

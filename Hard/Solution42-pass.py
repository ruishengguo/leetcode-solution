# 42、接雨水
import random
from typing import List


class Solution:
    def prefMax(self, lst: List[int]) -> List[int]:
        pref_max = [lst[0]]
        for i in range(2, len(lst)):
            pref_max.append(max(lst[i - 1], pref_max[i - 2]))
        return pref_max

    def suffMax(self, lst: List[int]) -> List[int]:
        suff_max = [lst[-1]]
        for i in range(-3, -len(lst) - 1, -1):
            suff_max.insert(0, max(lst[i + 1], suff_max[i + 2]))
        return suff_max

    def trap(self, height: List[int]) -> int:
        suff_max = self.suffMax(height)
        pref_max = self.prefMax(height)
        sum = 0
        for i in range(1, len(height) - 1):
            now = min(pref_max[i - 1], suff_max[i]) - height[i]
            if now > 0:
                sum += now
        return sum

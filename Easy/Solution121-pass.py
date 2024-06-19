# 121、买卖股票的最佳时机
from typing import List


class Solution:
    def prefMin(self, lst: List[int]) -> List[int]:
        pref_min = [lst[0]]
        for i in range(2, len(lst)):
            pref_min.append(min(lst[i - 1], pref_min[i - 2]))
        return pref_min

    def maxProfit(self, prices: List[int]) -> int:
        mins = self.prefMin(prices)
        max_P = 0
        for i in range(1, len(prices)):
            max_P = max(max_P, prices[i] - mins[i - 1])
        return max_P

# 1975、最大方阵和
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        elements = []
        for i in matrix:
            elements.extend(i)
        neg = []
        zero = False
        min_ = 100001
        max_ = -100001
        for i, num in enumerate(elements):
            if num < 0:
                neg.append(num)
                elements[i] = 0
                max_ = max(num, max_)
            elif num == 0:
                zero = True
            else:
                min_ = min(min_, num)

        res = sum(elements) - sum(neg)
        if len(neg) % 2 == 0 or zero:
            return res
        else:
            n = min(min_, -max_)
            return res - 2 * n

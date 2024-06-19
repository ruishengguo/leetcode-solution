# 682、棒球比赛
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == 'C':
                res.pop(-1)
            elif i == 'D':
                res.append(res[-1] * 2)
            elif i == '+':
                res.append(sum(res[-2:]))
            else:
                res.append(int(i))
        return sum(res)

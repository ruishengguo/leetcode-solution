# 1266、访问所有点的最小时间
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        temp = points[0]
        res = 0
        for i in points[1:]:
            res += max((abs(i[0] - temp[0]), abs(i[1] - temp[1])))
            temp = i
        return res

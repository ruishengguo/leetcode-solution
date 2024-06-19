# 883、三维形体投影面积
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        for i in grid:
            res += max(i)
            for j in i:
                if j:
                    res += 1
        z = {}
        for i in grid:
            for j in range(len(i)):
                if j not in z:
                    z[j] = i[j]
                else:
                    z[j] = max(z[j], i[j])
        for i in z:
            res += z[i]
        return res

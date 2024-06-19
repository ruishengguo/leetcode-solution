# 1037、有效的回旋镖
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1 = []
        for i in points:
            i = tuple(i)
            if i in p1:
                return False
            p1.append(i)
        dx1 = points[1][0] - points[0][0]
        dx2 = points[2][0] - points[0][0]
        dy1 = points[1][1] - points[0][1]
        dy2 = points[2][1] - points[0][1]
        if dx1 == 0:
            k1 = 'inf'
        else:
            k1 = dy1 / dx1
        if dx2 == 0:
            k2 = 'inf'
        else:
            k2 = dy2 / dx2
        if k1 == k2:
            return False
        return True

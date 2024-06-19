# 593、有效的正方形
from typing import Tuple, List


class Solution:
    def validSquareInOrder(self, p1_2: Tuple[List[int], List[int]], p3_4: Tuple[List[int], List[int]]):
        v1, v2 = (p1_2[1][0] - p1_2[0][0], p1_2[1][1] - p1_2[0][1]), (p3_4[1][0] - p3_4[0][0], p3_4[1][1] - p3_4[0][1])
        if not v1 == v2:
            return False
        v3 = (p3_4[0][0] - p1_2[0][0], p3_4[0][1] - p1_2[0][1])
        return v1[0] * v3[0] + v1[1] * v3[1] == 0 and v3[0] ** 2 + v3[1] ** 2 == v1[0] ** 2 + v1[1] ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        s = {tuple(p1), tuple(p2), tuple(p3), tuple(p4)}
        if len(s) != 4:
            return False
        for i in (((p1, p2), (p3, p4)), ((p1, p2), (p4, p3)), ((p1, p3), (p2, p4)), ((p1, p3), (p4, p2)), ((p2, p3), (p1, p4)), ((p2, p3), (p4, p1))):
            if self.validSquareInOrder(i[0], i[1]):
                return True
        return False

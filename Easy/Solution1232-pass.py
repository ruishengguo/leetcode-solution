# 1232、缀点成线
from typing import List


class Solution:
    def __init__(self):
        self.base_x = 0
        self.base_y = 0

    def getK(self, next_pos):
        dx = next_pos[0] - self.base_x
        dy = next_pos[1] - self.base_y
        if dx == 0:
            return 'inf'
        else:
            return dy / dx

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        self.base_x, self.base_y = coordinates[0][0], coordinates[0][1]
        k0 = self.getK(coordinates[1])
        for i in coordinates[2:]:
            ki = self.getK(i)
            if ki != k0:
                return False
        return True

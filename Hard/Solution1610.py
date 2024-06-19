# 1610、可见点的最大数目
import math
from typing import List


class Solution:
    def angle(self, p1: List[int], p2: List[int]):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx == 0 and dy == 0:
            return '?'
        if dx == 0:
            if dy < 0:
                return 270
            else:
                return 90
        elif dy == 0:
            if dx < 0:
                return 180
            else:
                return 0
        else:
            length = (dx ** 2 + dy ** 2) ** 0.5
            if dx > 0 and dy > 0:
                return round(math.degrees(math.acos(dx / length)), 8)
            elif dx < 0 and dy > 0:
                return round(180 - math.degrees(math.acos(dx / length)), 8)
            elif dx < 0 and dy < 0:
                return round(180 + math.degrees(math.acos(dx / length)), 8)
            return round(360 - math.degrees(math.acos(dx / length)), 8)

    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        points = list(map(lambda x: self.angle(location, x), points))
        res = points.count('?')
        while '?' in points:
            points.remove('?')
        points = sorted(points)
        pref = 360 - angle
        index = 0
        for i in points:
            if i >= pref:
                points = list(map(lambda x: x - 360, points[index:])) + points
                break
            index += 1
        index2, max_, l = 0, 1, len(points)
        for index1, item in enumerate(points):
            while points[index2] - item <= angle:
                index2 += 1
                if index2 == l:
                    break
            index2 -= 1
            max_ = max(index2 - index1 + 1, max_)
        return max_ + res


s = Solution()
print(s.visiblePoints([[34,26],[35,95],[31,56],[84,75],[26,76],[22,15],[26,78],[90,41],[94,18],[12,88],[42,82],[27,0],[85,49],[69,71],[13,36],[59,58],[58,18],[21,62]], 15, [67,91]))

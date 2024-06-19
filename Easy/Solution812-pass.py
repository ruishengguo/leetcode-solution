# 812、最大三角形面积


class Solution:
    def getArea(self, point1, point2, point3):
        return abs(point1[0] * (point2[1] - point3[1]) + point3[0] * (point1[1] - point2[1]) + point2[0] * (point3[1] - point1[1]))

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_ = 0
        for i1 in range(len(points)):
            for i2 in range(i1 + 1, len(points)):
                for i3 in range(i2 + 1, len(points)):
                    max_ = max(self.getArea(points[i1], points[i2], points[i3]), max_)
        return max_ / 2

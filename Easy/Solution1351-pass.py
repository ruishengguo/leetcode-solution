# 1351、统计有序矩阵中的负数
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        temp = len(grid[0]) - 1
        col, right = 0, temp
        res = 0
        for i in grid[::-1]:
            for j in i[col:][::-1]:
                if j >= 0:
                    if right == temp:
                        return res
                    col, right = right, temp
                    break
                else:
                    res += 1
                    right -= 1
        return res

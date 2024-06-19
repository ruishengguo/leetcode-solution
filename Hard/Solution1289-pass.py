# 1289、下降路径最小和II
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        l = len(grid)
        for i in range(l - 1):
            index, min_ = 0, [20000, 20000]
            for j, num in enumerate(grid[i]):
                if num < min_[1]:
                    if num < min_[0]:
                        min_[0], index, min_[1] = num, j, min_[0]
                    else:
                        min_[1] = num
            for j in range(l):
                if j != index:
                    grid[i + 1][j] += min_[0]
                else:
                    grid[i + 1][j] += min_[1]
        return min(grid[-1])

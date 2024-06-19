# 931、下降路径最小和
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l = len(matrix)
        for i in range(1, l):
            for j in range(l):
                situation = matrix[i - 1][j]
                if j != 0:
                    situation = min(situation, matrix[i - 1][j - 1])
                if j != l - 1:
                    situation = min(situation, matrix[i - 1][j + 1])
                matrix[i][j] += situation
        return min(matrix[-1])

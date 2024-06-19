# 1380、矩阵中的幸运数
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row, col = [10 ** 5] * len(matrix), [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row[i] = min(row[i], matrix[i][j])
                col[j] = max(col[j], matrix[i][j])
        res = []
        for i in row:
            if i in col:
                res.append(i)
        return res

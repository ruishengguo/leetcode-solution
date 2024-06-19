# 566、重塑矩阵
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        res = []
        mat1 = []
        for i in mat:
            mat1 += i
        for i in range(r):
            res.append(mat1[c * i:c * (i + 1)])
        return res

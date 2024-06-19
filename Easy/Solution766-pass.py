# 766、托普利茨矩阵
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        temp = tuple(matrix[0][:-1])
        for i in matrix[1:]:
            if tuple(i[1:]) != temp:
                return False
            temp = tuple(i[:-1])
        return True

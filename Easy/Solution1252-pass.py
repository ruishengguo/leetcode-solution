# 1252、奇数值单元格的数目
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for i in indices:
            rows[i[0]] ^= 1
            cols[i[1]] ^= 1
        c, r = sum(cols), sum(rows)
        return (n - c) * r + (m - r) * c

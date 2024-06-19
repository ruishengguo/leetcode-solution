# 119、杨辉三角II
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_lst = [1]
        for i in range(rowIndex):
            new_lst = [1, 1]
            for j in range(i):
                new_lst.insert(j + 1, row_lst[j] + row_lst[j + 1])
            row_lst = [] + new_lst
        return row_lst

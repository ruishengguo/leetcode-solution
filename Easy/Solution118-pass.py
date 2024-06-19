# 118、杨辉三角
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row_lst = [1]
        all_ = [[1]]
        for i in range(numRows - 1):
            new_lst = [1, 1]
            for j in range(i):
                new_lst.insert(j + 1, row_lst[j] + row_lst[j + 1])
            row_lst = [] + new_lst
            all_.append(row_lst)
        return all_

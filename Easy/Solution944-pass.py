# 944、删列造序
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        m, n = len(strs), len(strs[0])
        for col in range(n):
            for row in range(m - 1):
                if strs[row][col] > strs[row + 1][col]:
                    delete += 1
                    break
        return delete

# 1337、矩阵中战斗力最弱的 K 行
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            mat[i] = sum(mat[i])
        for i in range(min(mat), max(mat) + 1):
            for j in range(len(mat)):
                if i == mat[j]:
                    res.append(j)
                    if len(res) == k:
                        return res


s = Solution()
print(s.kWeakestRows([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 1))

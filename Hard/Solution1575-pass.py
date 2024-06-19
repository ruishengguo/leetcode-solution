# 1575、统计所有可行路径
import time
from typing import List


class Solution:
    # def __init__(self):
    #     self.mat = []

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mat = []
        n = len(locations)
        addition = [0] * (fuel + 1)
        for i in range(n):
            mat.append(addition[:])

        for i in range(fuel + 1):
            mat[finish][i] = 1

        for f in range(min(locations) - 2, fuel + 1):
            for row in range(n):
                if f == 0 and row != finish:
                    continue
                for pos in range(n):
                    if pos == row:
                        continue
                    need = abs(locations[pos] - locations[row])
                    if f >= need:
                        mat[row][f] += mat[pos][f - need]
        return mat[start][fuel] % 1000000007


'''
        n = len(locations)
        addition = [0] * n
        for i in range(n):
            self.mat.append(addition[:])
        for i in range(n):
            for j in range(i + 1, n):
                delta = abs(locations[i] - locations[j])
                self.mat[i][j], self.mat[j][i] = delta, delta
        return self.dfs(start, finish, fuel)

    def dfs(self, now: int, finish: int, fuel: int) -> int:
        sum_ = 0
        if now == finish:
            sum_ += 1
        if self.mat[now][finish] > fuel:
            return sum_
        for i, need in enumerate(self.mat[now]):
            if need == 0:
                continue
            elif need <= fuel:
                sum_ += self.dfs(i, finish, fuel - need)
        return sum_
'''

s = Solution()
t = time.time()
print(s.countRoutes([6, 5, 4, 7, 20], 0, 4, 65272))
print(time.time() - t)
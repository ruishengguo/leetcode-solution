# 1162、地图分析
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = 1
        map_ = {'land': set(), 'ocean': set()}
        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    map_['land'].add((row_index, col_index))
                else:
                    map_['ocean'].add((row_index, col_index))
        if len(map_['land']) == 0 or len(map_['ocean']) == 0:
            return -1
        m, n = len(grid), len(grid[0])
        while True:
            update = set()
            for i in map_['land']:
                for j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    new = (i[0] + j[0], i[1] + j[1])
                    if new[0] < 0 or new[0] >= m or new[1] < 0 or new[1] >= n:
                        continue
                    update.add(new)
            map_['ocean'] -= update
            if not map_['ocean']:
                return res
            res += 1
            map_['land'] = map_['land'].union(update)

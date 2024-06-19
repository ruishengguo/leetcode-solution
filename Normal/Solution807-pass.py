# 807、保持城市天际线
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        before = 0
        after = 0
        length = len(grid)
        cols = []
        col_remain = length
        rows = []
        rows_remain = length
        for i in range(length):
            rows.append(max(grid[i]))
            c = []
            for j in range(length):
                c.append(grid[j][i])
                before += grid[i][j]
            cols.append(max(c))
        cols = sorted(cols)
        rows = sorted(rows)
        for i in range(2 * length):
            if col_remain > 0:
                c = cols[0]
            else:
                break
            if rows_remain > 0:
                r = rows[0]
            else:
                break
            if c > r:
                after += r * col_remain
                rows_remain -= 1
                rows.pop(0)
            else:
                after += c * rows_remain
                col_remain -= 1
                cols.pop(0)
        return after - before

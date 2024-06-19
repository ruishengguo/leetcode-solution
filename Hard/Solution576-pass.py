# 576、出界的路径数


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        array = [0] * (maxMove + 1)
        mat = []
        for i in range(m):
            row = []
            for i in range(n):
                row.append(array[:])
            mat.append(row[:])
        # mat[row][col][move]: 在第row行col列处使用恰好move步可以出界的路径数
        # 边界处加1
        for i in range(m):
            mat[i][0][1] += 1
            mat[i][-1][1] += 1
        for j in range(n):
            mat[0][j][1] += 1
            mat[-1][j][1] += 1
        for move in range(2, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    # 加上周围数字
                    if row != 0:
                        mat[row][col][move] += mat[row - 1][col][move - 1]
                    if col != 0:
                        mat[row][col][move] += mat[row][col - 1][move - 1]
                    if row != m - 1:
                        mat[row][col][move] += mat[row + 1][col][move - 1]
                    if col != n - 1:
                        mat[row][col][move] += mat[row][col + 1][move - 1]
        return sum(mat[startRow][startColumn]) % 1000000007

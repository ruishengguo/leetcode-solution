# 1301、最大得分的路径数目
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        cell = [0, 0]
        mat = []
        for i in range(m):
            row = []
            for j in range(m):
                row.append(cell[:])
            mat.append(row[:])
        board[0] = '0' + board[0][1:]
        for row in range(m - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if board[row][col] == 'S':
                    mat[row][col] = [0, 1]
                elif board[row][col] == 'X':
                    mat[row][col] = [0, 0]
                else:
                    if col == m - 1:
                        mat[row][col] = [mat[row + 1][col][0] + int(board[row][col]), mat[row + 1][col][1]]
                    elif row == m - 1:
                        mat[row][col] = [mat[row][col + 1][0] + int(board[row][col]), mat[row][col + 1][1]]
                    elif board[row + 1][col] + board[row][col + 1] == 'XX':
                        mat[row][col] = [mat[row + 1][col + 1][0] + int(board[row][col]), mat[row + 1][col + 1][1]]
                    else:
                        for i in (mat[row + 1][col], mat[row][col + 1]):
                            if i[0] > mat[row][col][0]:
                                mat[row][col] = i[:]
                            elif i[0] == mat[row][col][0]:
                                mat[row][col][1] += i[1]
                        mat[row][col][0] += int(board[row][col])
        return [mat[0][0][0] % 1000000007, mat[0][0][1] % 1000000007]


s = Solution()
print(s.pathsWithMaxScore(["E23","2X2","12S"]))

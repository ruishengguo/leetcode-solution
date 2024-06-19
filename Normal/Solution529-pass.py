# 529、扫雷游戏
from typing import List, Tuple

around = {(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)}


class Solution:
    def spread(self, board: List[List[str]], click: Tuple[int], m: int, n: int, passed: set) -> set:
        num = 0
        next_cells = set()
        for i in around:
            nxt = (click[0] + i[0], click[1] + i[1])
            if nxt in passed:
                continue
            if -1 < nxt[0] < m and -1 < nxt[1] < n:
                if board[nxt[0]][nxt[1]] == 'M':
                    num += 1
                else:
                    next_cells.add(nxt)
        if num:
            board[click[0]][click[1]] = str(num)
            return {tuple(click)}
        else:
            board[click[0]][click[1]] = 'B'
            passed.add(click)
            for i in next_cells:
                passed = passed.union(self.spread(board, i, m, n, passed))
            return passed

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        new = []
        types = {'M': set(), 'E': set(), 'B': set()}
        for row, i in enumerate(board):
            new.append([])
            for col, j in enumerate(i):
                k = j if j in 'MEB' else 'B'
                new[row].append(j)
                types[k].add((row, col))
        if tuple(click) in types['B']:
            return board
        elif tuple(click) in types['M']:
            for cell in types['M']:
                new[cell[0]][cell[1]] = 'X'
            return new
        else:
            self.spread(new, tuple(click), len(new), len(new[0]), {tuple(click)})
            return new

# 1275、找出井字棋的获胜者
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) <= 4:
            return 'Pending'
        # A
        rows, cols = [0, 0, 0], [0, 0, 0]
        crossing1, crossing2 = [0], [0]
        for i in moves[::2]:
            rows[i[0]] += 1
            cols[i[1]] += 1
            if i[0] == i[1]:
                crossing1[0] += 1
            if i[0] + i[1] == 2:
                crossing2[0] += 1
        for i in (rows, cols, crossing1, crossing2):
            if 3 in i:
                return 'A'
        # B
        rows, cols = [0, 0, 0], [0, 0, 0]
        crossing1, crossing2 = [0], [0]
        for i in moves[1::2]:
            rows[i[0]] += 1
            cols[i[1]] += 1
            if i[0] == i[1]:
                crossing1[0] += 1
            if i[0] + i[1] == 2:
                crossing2[0] += 1
        for i in (rows, cols, crossing1, crossing2):
            if 3 in i:
                return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'

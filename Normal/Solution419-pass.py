from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        result = 0
        for _ in range(row):
            for __ in range(col):
                if board[_][__] == 'X':
                    result += 1
                    board[_][__] = '.'
                    c = __ + 1
                    while c < col:
                        if board[_][c] == 'X':
                            board[_][c] = '.'
                            c += 1
                        else:
                            break
                    r = _ + 1
                    while r < row:
                        if board[r][__] == 'X':
                            board[r][__] = '.'
                            r += 1
                        else:
                            break
        return result

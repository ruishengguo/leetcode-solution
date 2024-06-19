# 37、解数独
from typing import List


class Solution:
    nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    """
    col(board[...][col])
    #  #  # | #  #  # | #  #  # row(board[row][...])
    #  #  # | #  #  # | #  #  #
    #  #  # | #  #  # | #  #  # 3*3:pal(row // 3 * 3 + col // 3)
    ---------------------------
    #  #  # | #  #  # | #  #  #
    #  #  # | #  #  # | #  #  #
    #  #  # | #  #  # | #  #  #
    ---------------------------
    #  #  # | #  #  # | #  #  #
    #  #  # | #  #  # | #  #  #
    #  #  # | #  #  # | #  #  #
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        col_hash = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        squ_hash = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        for row in range(9):
            for col in range(9):
                node = board[row][col]
                if node == '.':
                    continue
                squ = 3 * (row // 3) + col // 3
                if node not in row_hash[row]:
                    row_hash[row].add(node)
                else:
                    return False
                if node not in col_hash[col]:
                    col_hash[col].add(node)
                else:
                    return False
                if node not in squ_hash[squ]:
                    squ_hash[squ].add(node)
                else:
                    return False
        return True

    def __init__(self) -> None:
        self.groups = {'rows': [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                       'cols': [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                       'pals': [set(), set(), set(), set(), set(), set(), set(), set(), set()]}
        self.cells = {}
        self.board = [["."]]

    def sort(self, board: List[List[str]]) -> None:
        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                if cell == '.':
                    self.cells[(rowIndex, colIndex)] = set()
                else:
                    self.groups['rows'][rowIndex].add(cell)
                    self.groups['cols'][colIndex].add(cell)
                    self.groups['pals'][Solution.get_palace_index(rowIndex, colIndex)].add(cell)
        self.update_on_cells()

    @staticmethod
    def get_palace_index(row, col) -> int:
        return row // 3 * 3 + col // 3

    def update(self) -> None:
        do_return = False
        complete = set()
        for i in self.cells:
            if len(self.cells[i]) == 1:
                do_return = True
                val = list(self.cells[i])[0]
                self.board[i[0]][i[1]] = val
                self.groups['rows'][i[0]].add(val)
                self.groups['cols'][i[1]].add(val)
                self.groups['pals'][Solution.get_palace_index(i[0], i[1])].add(val)
                complete.add(i)
        if do_return:
            for i in complete:
                self.cells.pop(i)
            self.update_on_cells()
            self.update()

    def update_on_cells(self) -> None:
        for blank in self.cells:
            self.cells[blank] = Solution.nums - self.groups['rows'][blank[0]].\
                                union(self.groups['cols'][blank[1]]).union(
                                self.groups['pals'][Solution.get_palace_index(blank[0], blank[1])])

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.sort(self.board)
        self.update()
        if not self.isValidSudoku(self.board):
            board[0] = ['.']
            return
        for i in self.cells:
            for j in self.cells[i]:
                new_board = list(map(lambda x: x[:], self.board))
                new_board[i[0]][i[1]] = j
                branch = Solution()
                branch.solveSudoku(new_board)
                if Solution.detect(new_board):
                    board[:] = new_board
                    return
            board[0] = ['.']
            return

    @staticmethod
    def detect(board: List[List[str]]) -> bool:
        for i in board:
            if '.' in i:
                return False
        return True

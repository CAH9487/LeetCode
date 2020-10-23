import unittest
from typing import Any, List
from collections import Counter
import itertools
from time import sleep


def show(board, row=-1, col=-1):
    print(chr(27) + "[2J")
    if(row != -1 and col != -1):
        t = board[row][col]
        board[row][col] = '＊'
    print('   ', end='')
    for x in range(9):
        print(f' {x}   ', end='')
    print('\n')
    row_n = 0
    for x in board:
        print(f'{row_n}  ', end='')
        row_n += 1
        for y in x:
            if(y == '＊'):
                s = f' {y}'
                print(f'{s} |', end='')
            else:
                s = f' {y} '
                print(f'{s} |', end='')
        print()
        print('－'*24)
    print()
    if(row != -1 and col != -1):
        board[row][col] = t


'''
Runtime: 40 ms, faster than 99.51% of Python3 online submissions
Memory Usage: 13.1 MB, less than 65.46% of Python3 online submissions
https://leetcode.com/problems/sudoku-solver/discuss/298365/Fast-Python-3-Solution-with-Comments-(40ms-faster-than-99.51)
'''
class Solution_RogerWWW:
    col_size = 9  # len(self.board)
    row_size = 9  # len(self.board[0])
    block_col_size = 3
    block_row_size = 3
    digits = '123456789'
    empty_symbol = '.'

    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        self.init(board)
        self.solve()

    def init(self, board):
        self.board = board

        # list all empty cells. a `cell` is a tuple `(row_index, col_index)`
        self.empty_cells = set([(ri, ci) for ri in range(self.row_size) for ci in range(self.col_size) if self.board[ri][ci] == self.empty_symbol])

        # find candidates of each cell
        self.candidates = [[set(self.digits) for ci in range(self.col_size)] for ri in range(self.row_size)]
        for ri in range(self.row_size):
            for ci in range(self.col_size):
                digit = self.board[ri][ci]
                if digit != self.empty_symbol:
                    self.candidates[ri][ci] = set()
                    self.update_candidates((ri, ci), digit)

    def solve(self):
        # if there are no empty cells, it's solved
        if not self.empty_cells:
            return True

        # get the cell with fewest candidates
        cell = min(self.empty_cells, key=lambda cell: len(self.candidates[cell[0]][cell[1]]))

        # try filling the cell with one of the candidates, and solve recursively
        ri, ci = cell
        for digit in list(self.candidates[ri][ci]):
            candidate_updated_cells = self.fill_cell(cell, digit)
            solved = self.solve()
            if solved:
                return True
            self.unfill_cell(cell, digit, candidate_updated_cells)

        # if no solution found, go back and try the next candidates
        return False

    def fill_cell(self, cell, digit):
        # fill the cell with the digit
        ri, ci = cell
        self.board[ri][ci] = digit

        # remove the cell from empty_cells
        self.empty_cells.remove(cell)

        # update the candidates of other cells
        # keep a list of updated cells. will be used when unfilling cells
        candidate_updated_cells = self.update_candidates(cell, digit)

        return candidate_updated_cells

    def unfill_cell(self, cell, digit, candidate_updated_cells):
        # unfill cell
        ri, ci = cell
        self.board[ri][ci] = self.empty_symbol

        # add the cell back to empty_cells
        self.empty_cells.add(cell)

        # add back candidates of other cells
        for ri, ci in candidate_updated_cells:
            self.candidates[ri][ci].add(digit)

    def update_candidates(self, filled_cell, digit):
        candidate_updated_cells = []
        for ri, ci in self.related_cells(filled_cell):
            if (self.board[ri][ci] == self.empty_symbol) and (digit in self.candidates[ri][ci]):
                self.candidates[ri][ci].remove(digit)
                candidate_updated_cells.append((ri, ci))
        return candidate_updated_cells

    def related_cells(self, cell):
        return list(set(self.cells_in_same_row(cell) + self.cells_in_same_col(cell) + self.cells_in_same_block(cell)))

    def cells_in_same_row(self, cell):
        return [(cell[0], ci) for ci in range(self.col_size)]

    def cells_in_same_col(self, cell):
        return [(ri, cell[1]) for ri in range(self.row_size)]

    def cells_in_same_block(self, cell):
        block_first_cell_ri = (cell[0] // self.block_row_size) * self.block_row_size
        block_first_cell_ci = (cell[1] // self.block_col_size) * self.block_col_size
        return [
            (block_first_cell_ri + in_block_ri, block_first_cell_ci + in_block_ci)
            for in_block_ri in range(self.block_row_size)
            for in_block_ci in range(self.block_col_size)
        ]

'''
Runtime: 692 ms, faster than 25.32% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
https://www.itread01.com/content/1544422522.html
'''
class Solution_DFS:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def isValid(x,y):
            tmp=board[x][y]
            board[x][y]='D'
            for i in range(9):
                if board[i][y]==tmp: 
                    return False
            for i in range(9):
                if board[x][i]==tmp: 
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j]==tmp: 
                        return False
            board[x][y]=tmp
            return True
        
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i][j]=k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j]='.'
                        return False
            return True
        dfs(board)

'''
Runtime: 1100 ms, faster than 7.17% of Python3 online submissions
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for y, x in itertools.product(range(9), range(9)):
            if(board[y][x] == '.'):
                valid_nums = self.get_valid_num(board, y, x)
                if(not valid_nums):
                    return
                for n in valid_nums:
                    board[y][x] = n
                    self.solveSudoku(board)
                    if(self.check_finish(board)):
                        return
                    else:
                        board[y][x] = '.'
                        continue
                return

    def check_finish(self, board: List[List[str]]) -> bool:
        for x in board:
            for y in x:
                if(y == '.'):
                    return False
        return True

    def get_valid_num(self, board: List[List[str]], row: int, col: int) -> List[str]:
        if(board[row][col] != '.'):
            return []
        res = []
        for n in '123456789':
            board[row][col] = n
            if(self.isValidXY(board, row, col)):
                res.append(n)
            board[row][col] = '.'
        return res

    def isValidXY(self, board: List[List[str]], row: int, col: int) -> bool:
        # check row
        if(not self.check_array(board[row])):
            return False
        # check col
        arr = []
        for r in range(0, 9):
            arr.append(board[r][col])
        if(not self.check_array(arr)):
            return False
        # check sub-board
        arr = set()
        for r in range((row//3)*3, (row//3+1)*3):
            for c in range((col // 3)*3, (col // 3+1)*3):
                n = board[r][c]
                if(n == '.'):
                    continue
                if(n in arr):
                    return False
                else:
                    arr.add(n)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if(not self.check_array(row)):
                return False
        for col in list(map(list, zip(*board))):
            if(not self.check_array(col)):
                return False
        for subidx in range(9):
            b = set()
            for row in range((subidx//3)*3, (subidx//3+1)*3):
                for col in range((subidx % 3)*3, (subidx % 3+1)*3):
                    if(board[row][col] == '.'):
                        continue
                    if(board[row][col] in b):
                        return False
                    else:
                        b.add(board[row][col])
        return True

    # def get_subboard(self, board: List[List[str]], idx: int) -> List[str]:
    #     b = []
    #     for row in range((idx//3)*3, (idx//3+1)*3):
    #         for col in range((idx % 3)*3, (idx % 3+1)*3):
    #             b.append(board[row][col])
    #     return b

    def check_array(self, arr: List[str]) -> bool:
        d = set()
        for x in arr:
            if(x == '.'):
                continue
            if(x not in d):
                d.add(x)
            else:
                return False
        return True
        

import copy
import time
class TestCase(unittest.TestCase):
    sln = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    ans = [["5","3","4","6","7","8","9","1","2"],
           ["6","7","2","1","9","5","3","4","8"],
           ["1","9","8","3","4","2","5","6","7"],
           ["8","5","9","7","6","1","4","2","3"],
           ["4","2","6","8","5","3","7","9","1"],
           ["7","1","3","9","2","4","8","5","6"],
           ["9","6","1","5","3","7","2","8","4"],
           ["2","8","7","4","1","9","6","3","5"],
           ["3","4","5","2","8","6","1","7","9"]]
    
    def test_1(self):
        board_copy = copy.deepcopy(self.board)
        self.sln.solveSudoku(board_copy)
        self.assertEqual(board_copy, self.ans)

    def test_performance(self):
        time_total = 0.0
        for _ in range(10):
            board_copy = copy.deepcopy(self.board)
            time_start = time.time()
            self.sln.solveSudoku(board_copy)
            time_total += time.time() - time_start
        self.assertLessEqual(time_total, 15)


if __name__ == '__main__':
    unittest.main()
    # board = [["5","3",".",".","7",".",".",".","."],
    #          ["6",".",".","1","9","5",".",".","."],
    #          [".","9","8",".",".",".",".","6","."],
    #          ["8",".",".",".","6",".",".",".","3"],
    #          ["4",".",".","8",".","3",".",".","1"],
    #          ["7",".",".",".","2",".",".",".","6"],
    #          [".","6",".",".",".",".","2","8","."],
    #          [".",".",".","4","1","9",".",".","5"],
    #          [".",".",".",".","8",".",".","7","9"]]
    # ans = [["5","3","4","6","7","8","9","1","2"],
    #        ["6","7","2","1","9","5","3","4","8"],
    #        ["1","9","8","3","4","2","5","6","7"],
    #        ["8","5","9","7","6","1","4","2","3"],
    #        ["4","2","6","8","5","3","7","9","1"],
    #        ["7","1","3","9","2","4","8","5","6"],
    #        ["9","6","1","5","3","7","2","8","4"],
    #        ["2","8","7","4","1","9","6","3","5"],
    #        ["3","4","5","2","8","6","1","7","9"]]
    # sln = Solution()
    # for _ in range(10):
    #     board_copy = copy.deepcopy(board)
    #     sln.solveSudoku(board_copy)
    # # print(board == ans)
    # # show(board)

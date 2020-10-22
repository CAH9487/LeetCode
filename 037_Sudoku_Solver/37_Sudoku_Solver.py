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
        for _ in range(100):
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
    # sln.solveSudoku(board)
    # print(board == ans)
    # show(board)

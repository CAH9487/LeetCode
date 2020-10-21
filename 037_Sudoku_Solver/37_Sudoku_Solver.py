import unittest
from typing import Any, List
from collections import Counter
import itertools
from time import sleep


def show(board, row, col):
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


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        '''
        Time Limit Exceeded
        '''
        if(self.check_finish(board)):
            return
        for y, x in itertools.product(range(9), range(9)):
            if(board[y][x] == '.'):
                valid_nums = self.get_valid_num(board, y, x)
                # print(chr(27) + "[2J")
                # print(f'({y}, {x}), valid_nums = {valid_nums}')
                # show(board, y, x)
                # sleep(0.02)
                # input()
                if(not valid_nums):
                    return
                for n in valid_nums:
                    board[y][x] = str(n)
                    # print(chr(27) + "[2J")
                    # print()
                    # show(board, -1, -1)
                    # sleep(0.02)
                    # input()
                    self.solveSudoku(board)
                    if(self.check_finish(board)):
                        return
                    else:
                        board[y][x] = '.'
                        continue
                return

    @staticmethod
    def check_finish(board: List[List[str]]) -> bool:
        if(SudokuValider.isValidSudoku(board)):
            for x in board:
                for y in x:
                    if(y == '.'):
                        return False
            return True
        return False

    @staticmethod
    def get_valid_num(board: List[List[str]], row: int, col: int) -> List[str]:
        if(board[row][col] != '.'):
            return []
        res = []
        for n in range(1, 9+1):
            board[row][col] = str(n)
            if(SudokuValider.isValidSudoku(board)):
                res.append(str(n))
            board[row][col] = '.'
        return res


class SudokuValider:
    @classmethod
    def isValidSudoku(cls, board: List[List[str]]) -> bool:
        for row in board:
            if(not cls.check_array(row)):
                return False
        for col in list(map(list, zip(*board))):
            if(not cls.check_array(col)):
                return False
        for subidx in range(9):
            if(not cls.check_array(cls.get_subboard(board, subidx))):
                return False
        return True

    @staticmethod
    def get_subboard(board: List[List[str]], idx: int) -> List[str]:
        b = []
        for col in range((idx//3)*3, (idx//3+1)*3):
            for row in range((idx % 3)*3, (idx % 3+1)*3):
                b.append(board[col][row])
        return b

    @staticmethod
    def check_array(arr: List[str]) -> bool:
        count = Counter(arr)
        for x in count:
            if(x == '.'):
                continue
            try:
                n = int(x)
            except:
                return False

            if(not (1 <= n <= 9)):
                return False
            if(count[x] > 1):
                return False
        return True
        

class TestCase(unittest.TestCase):
    def test_1(self):
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
        sln.solveSudoku(board)
        self.assertEqual(board, ans)


if __name__ == '__main__':
    unittest.main()
    # tc = TestCase()
    # tc.test_1()
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
    # show(board, -1, -1)

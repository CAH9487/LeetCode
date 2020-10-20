import unittest
from typing import Any, List
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if(not self.check_array(row)):
                return False
        for col in list(map(list, zip(*board))):
            if(not self.check_array(col)):
                return False

        return True

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
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(sln.isValidSudoku(board), True)

    def test_2(self):
        sln = Solution()
        board = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]
        self.assertEqual(sln.isValidSudoku(board), False)


if __name__ == '__main__':
    unittest.main()
    # tc = TestCase()
    # tc.test_1()

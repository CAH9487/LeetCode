import unittest
from typing import Any, List


'''
Runtime: 60 ms, faster than 68.88% of Python3 online submissions
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        status = 0
        profit = 0
        cost = 0
        for i in range(len(prices)):
            if(status == 0):
                if(i != len(prices)-1 and prices[i] < prices[i+1]):
                    cost = prices[i]
                    status = 1
            else:
                if(i == len(prices)-1):
                    profit += prices[i] - cost
                else:
                    if(prices[i+1] <= prices[i]):
                        profit += prices[i] - cost
                        cost = 0
                        status = 0
        return profit



class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        i = [7,1,5,3,6,4]
        o = 7
        res = self.sln.maxProfit(i)
        self.assertEqual(res, o)

    def test_2(self):
        i = [1,2,3,4,5]
        o = 4
        res = self.sln.maxProfit(i)
        self.assertEqual(res, o)

    def test_3(self):
        i = [7,6,4,3,1]
        o = 0
        res = self.sln.maxProfit(i)
        self.assertEqual(res, o)


if __name__ == '__main__':
    unittest.main()

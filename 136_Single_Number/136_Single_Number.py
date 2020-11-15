import unittest
from typing import Any, List
from collections import defaultdict

'''
Runtime: 132 ms, faster than 39.02% of Python3 online submissions
Memory Usage: 16.7 MB, less than 13.07% of Python3 online submissions
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(int)
        for i in range(n):
            d[nums[i]] += 1
        for k in d:
            if(d[k] == 1):
                return k
        return -1


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        d = [2,2,1]
        ans = 1
        res = self.sln.singleNumber(d)
        self.assertEqual(res, ans)

    def test_2(self):
        d = [4,1,2,1,2]
        ans = 4
        res = self.sln.singleNumber(d)
        self.assertEqual(res, ans)

    def test_3(self):
        d = [1]
        ans = 1
        res = self.sln.singleNumber(d)
        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()

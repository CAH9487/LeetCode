import unittest
from typing import Any, List


'''
Runtime: 120 ms, faster than 46.91% of Python3 online submissions
Memory Usage: 19 MB, less than 94.96% of Python3 online submissions
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(not nums):
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        d = [1, 2, 3, 1]
        res = self.sln.containsDuplicate(d)
        self.assertEqual(res, True)

    def test_2(self):
        d = [1, 2, 3, 4]
        res = self.sln.containsDuplicate(d)
        self.assertEqual(res, False)

    def test_3(self):
        d = []
        res = self.sln.containsDuplicate(d)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()

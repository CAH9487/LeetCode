import unittest
from typing import Any, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] == prev):
                prev = nums[i]
                nums.pop(i)
            else:
                prev = nums[i]
        return len(nums)


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        i = [1, 1, 2]
        o = [1, 2]
        l = 2
        res = self.sln.removeDuplicates(i)
        self.assertEqual(res, l)
        self.assertEqual(i, o)

    def test_2(self):
        i = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        o = [0, 1, 2, 3, 4]
        l = 5
        res = self.sln.removeDuplicates(i)
        self.assertEqual(res, l)
        self.assertEqual(i, o)


if __name__ == '__main__':
    unittest.main()

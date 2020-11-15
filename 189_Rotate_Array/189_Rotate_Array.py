import unittest
from typing import Any, List


'''
Runtime: 56 ms, faster than 87.94% of Python3 online submissions
Memory Usage: 15.4 MB, less than 27.03% of Python3 online submissions
'''
class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(not nums):
            return
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        o = [5, 6, 7, 1, 2, 3, 4]
        self.sln.rotate(nums, k)
        self.assertEqual(nums, o)

    def test_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        o = [3, 99, -1, -100]
        self.sln.rotate(nums, k)
        self.assertEqual(nums, o)

    def test_3(self):
        nums = [-1]
        k = 2
        o = [-1]
        self.sln.rotate(nums, k)
        self.assertEqual(nums, o)

    def test_4(self):
        nums = [1, 2]
        k = 3
        o = [2, 1]
        self.sln.rotate(nums, k)
        self.assertEqual(nums, o)


if __name__ == '__main__':
    unittest.main()

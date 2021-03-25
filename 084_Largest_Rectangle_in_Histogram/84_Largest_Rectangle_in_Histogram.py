import unittest
from typing import Any, List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            while(heights[i] < heights[stack[-1]]):
                idx = stack.pop()
                h = heights[idx]
                w = (i - 1) - stack[-1]
                area = max(area, h * w)
            stack.append(i)
        return area


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        bars = [2, 1, 5, 6, 2, 3]
        ans = 10
        res = self.sln.largestRectangleArea(bars)
        self.assertEqual(res, ans)
    
    def test_2(self):
        bars = [2, 4]
        ans = 4
        res = self.sln.largestRectangleArea(bars)
        self.assertEqual(res, ans)
    
    def test_3(self):
        bars = [2, 1, 2]
        ans = 3
        res = self.sln.largestRectangleArea(bars)
        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()

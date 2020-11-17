import unittest
from typing import Any, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Runtime: 36 ms, faster than 90.04% of Python3 online submissions
Memory Usage: 15.7 MB, less than 41.86% of Python3 online submissions
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(not root):
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return 1 + depth_left if depth_left > depth_right else 1 + depth_right


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        res = self.sln.maxDepth(tree)
        self.assertEqual(res, 3)

    def test_2(self):
        tree = None
        res = self.sln.maxDepth(tree)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()

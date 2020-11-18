import unittest
from typing import Any, List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
level order is palindrome
Runtime: 32 ms, faster than 78.16% of Python3 online submissions
Memory Usage: 14.3 MB, less than 14.17% of Python3 online submissions
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if(not root):
            return True
        seq = []
        queue = [(root, 1)]
        level = level_prev = 0
        while(queue):
            root, level = queue.pop(0)
            if(level != level_prev):
                if(not self.isPalindrome(seq)):
                    return False
                seq.clear()
                level_prev = level

            if(root):
                seq.append(root.val)
                queue.append((root.left, level+1))
                queue.append((root.right, level+1))
            else:
                seq.append(None)

        return self.isPalindrome(seq)

    def isPalindrome(self, s):
        return s == s[::-1]


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        res = self.sln.isSymmetric(tree)
        self.assertEqual(res, True)

    def test_2(self):
        tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        res = self.sln.isSymmetric(tree)
        self.assertEqual(res, False)

    def test_3(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(2), None), TreeNode(2, TreeNode(2), None))
        res = self.sln.isSymmetric(tree)
        self.assertEqual(res, False)

    def test_4(self):
        tree = TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, None)), None), TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
        res = self.sln.isSymmetric(tree)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
    # sln = Solution()
    # tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    # tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6), None), None), TreeNode(3, None, TreeNode(5, None, TreeNode(7))))
    # sln.isSymmetric(tree)

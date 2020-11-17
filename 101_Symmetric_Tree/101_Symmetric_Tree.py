import unittest
from typing import Any, List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if(not root):
            return True
        level_order_seq = self.level_order(root)
        print(level_order_seq)
        depth = math.floor(math.log(len(level_order_seq)+1, 2))
        for i in range(1, depth+1):
            start, end = 2**(i-1)-1, 2**(i)-1
            this_level = level_order_seq[start:end]
            if(self.isPalindrome(this_level) == False):
                return False
        return True

    def level_order(self, root):
        res = []
        if(not root):
            return [None]
        queue = [root]
        while(root or queue):
            root = queue.pop(0)
            if(root):
                res.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                res.append(None)
                continue

        return res

    def isPalindrome(self, s):
        return s == s[::-1]



class TestCase(unittest.TestCase):
    sln = Solution()

    # def test_1(self):
    #     tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    #     res = self.sln.isSymmetric(tree)
    #     self.assertEqual(res, True)

    # def test_2(self):
    #     tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    #     res = self.sln.isSymmetric(tree)
    #     self.assertEqual(res, False)

    # def test_3(self):
    #     tree = TreeNode(1, TreeNode(2, TreeNode(2), None), TreeNode(2, TreeNode(2), None))
    #     res = self.sln.isSymmetric(tree)
    #     self.assertEqual(res, False)

    def test_4(self):
        tree = TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, None)), None), TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
        res = self.sln.isSymmetric(tree)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()

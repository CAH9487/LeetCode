import unittest
from typing import Any, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Recursive Approach
Runtime: 44 ms, faster than 64.75% of Python3 online submissions
Memory Usage: 16.2 MB, less than 54.61% of Python3 online submissions
'''
class Solution_Recursive:
    def isValidBST(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        if(not root):
            return True
        if(root.val <= lower or root.val >= upper):
            return False
        if(self.isValidBST(root.left, lower, root.val) == False):
            return False
        if(self.isValidBST(root.right, root.val, upper) == False):
            return False
        return True

'''
Inorder Approach
Runtime: 52 ms, faster than 12.20% of Python3 online submissions
Memory Usage: 16.5 MB, less than 23.78% of Python3 online submissions
'''
class Solution_Inorder:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder_seq = self.inorder(root)
        for i in range(len(inorder_seq)-1):
            if(inorder_seq[i] >=  inorder_seq[i+1]):
                return False
        return True

    def inorder(self, root):
        res = []
        if(not root):
            return []
        res.extend(self.inorder(root.left))
        res.append(root.val)
        res.extend(self.inorder(root.right))
        return res


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        tree = TreeNode(2, TreeNode(1), TreeNode(3))
        res = self.sln.isValidBST(tree)
        self.assertEqual(res, True)

    def test_2(self):
        tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        res = self.sln.isValidBST(tree)
        self.assertEqual(res, False)

    def test_3(self):
        tree = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
        res = self.sln.isValidBST(tree)
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()

import unittest
from typing import Any, List
from collections import defaultdict


'''
Runtime: 536 ms, faster than 10.06% of Python3 online submissions
Memory Usage: 14.8 MB, less than 5.90% of Python3 online submissions
'''
class Solution:
    '''
    constrain: O(n)
    '''
    def minWindow(self, s: str, t: str) -> str:
        if(not s or not t):
            return ''

        map = defaultdict(lambda: 0)
        bag = defaultdict(lambda: 0)
        for c in t:
            map[c] += 1
            bag[c] = 0

        def check_match(x, y): return all(
            a <= b for a, b in zip(x.values(), y.values()))

        window = (len(s)+1, -1, -1)
        left = 0
        for right in range(len(s)):
            c = s[right]
            if(c in bag):
                bag[c] += 1

            while(left < right+1 and check_match(map, bag)):
                length = right - left + 1
                if(length < window[0]):
                    window = (length, left, right+1)
                c = s[left]
                if(c in bag):
                    bag[c] -= 1
                left += 1

        if(window[0] <= len(s)):
            return s[window[1]:window[2]]
        else:
            return ''



class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        S = "ADOBECODEBANC"
        T = "ABC"
        a = "BANC"
        r = self.sln.minWindow(S, T)
        self.assertEqual(r, a)

    def test_2(self):
        S = "ADOBECODEBANC"
        T = "XZY"
        a = ""
        r = self.sln.minWindow(S, T)
        self.assertEqual(r, a)

    def test_3(self):
        S = "a"
        T = "aa"
        a = ""
        r = self.sln.minWindow(S, T)
        self.assertEqual(r, a)

    def test_4(self):
        S = "cabwefgewcwaefgcf"
        T = "cae"
        a = "cwae"
        r = self.sln.minWindow(S, T)
        self.assertEqual(r, a)

    def test_4(self):
        S = "a"
        T = "a"
        a = "a"
        r = self.sln.minWindow(S, T)
        self.assertEqual(r, a)

if __name__ == '__main__':
    unittest.main()

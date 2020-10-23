import unittest
from typing import Any, List


class Solution:
    '''
    constrain: O(n)
    '''
    def minWindow(self, s: str, t: str) -> str:
        if(not s or not t):
            return ''

        map = {}
        for c in t:
            if(c in map):
                map[c][0] += 1
            else:
                # [count in t, index list]
                map[c] = [1, []]

        for i in range(len(s)):
            c = s[i]
            if(c in map):
                map[c][1].append(i)

        candidates = []
        for cnt, idx_list in map.values():
            if(len(idx_list) < cnt):
                return ''
            candidates.extend(idx_list[-cnt:])
        if(not candidates):
            return ''
        begin, end = min(candidates), max(candidates)
        result = s[begin:end+1]
        return result


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

if __name__ == '__main__':
    unittest.main()

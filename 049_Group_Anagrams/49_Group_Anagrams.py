import unittest
from typing import Any, List
import collections


class Solution_:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

'''
Runtime: 7648 ms, faster than 5.05% of Python3 online submissions
Memory Usage: 27.2 MB, less than 9.01% of Python3 online submissions
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        table = {}
        fea_list = []
        for x in strs:
            self.reset_table(table)
            for c in x:
                table[c] += 1
            fea_list.append(table.copy())

        result = []
        used = [False]*length
        for x in range(length):
            if(used[x]):
                continue
            same = [strs[x]]
            used[x] = True
            for y in range(x+1, length):
                if(not used[y] and fea_list[x] == fea_list[y]):
                    same.append(strs[y])
                    used[y] = True
            result.append(same)

        return result

    def reset_table(self, table: dict) -> None:
        for x in range(97, 97+26):
            table[chr(x)] = 0


class TestCase(unittest.TestCase):
    sln = Solution()

    def test_1(self):
        q = ["eat", "tea", "tan", "ate", "nat", "bat"]
        a = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        r = self.sln.groupAnagrams(q)
        self.assertEqual(self.check_equal(r, a), True)

    def test_2(self):
        q = ['']
        a = [['']]
        r = self.sln.groupAnagrams(q)
        self.assertEqual(self.check_equal(r, a), True)

    def test_3(self):
        q = ['a']
        a = [['a']]
        r = self.sln.groupAnagrams(q)
        self.assertEqual(self.check_equal(r, a), True)

    def test_performance(self):
        import time
        q = ["eat", "tea", "tan", "ate", "nat", "bat"]
        a = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        time_start = time.time()
        for x in range(1000000):
            self.sln.groupAnagrams(q)
        total_time = time.time() - time_start
        print('Total time: {:.2f} sec.'.format(total_time))

    def check_equal(self, a, b):
        for x in a:
            x.sort()
        for x in b:
            x.sort()
        for x in a:
            if(x not in b):
                return False
        return True


if __name__ == '__main__':
    unittest.main()

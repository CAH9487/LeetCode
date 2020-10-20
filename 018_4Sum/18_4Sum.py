from typing import Any, List


'''
Runtime: 116 ms, faster than 77.85% of Python3 online submissions
Memory Usage: 14.2 MB, less than 5.08% of Python3 online submissions
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    @classmethod
    def kSum(cls, nums: List[int], target: int, k: int) -> List[List[int]]:
        if(len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target):
            return []

        if(k == 2):
            return cls.twoSum(nums, target)

        result = []
        for idx in range(len(nums)-1):
            if idx == 0 or nums[idx - 1] != nums[idx]:
                for x in cls.kSum(nums[idx+1:], target-nums[idx], k-1):
                    result.append([nums[idx]] + x)
        return result

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        if(len(nums) < 2):
            return []
        hash_table = {}
        result = []
        for idx in range(len(nums)):
            if((target - nums[idx]) not in hash_table.keys()):
                if(nums[idx] in hash_table):
                    hash_table[nums[idx]].append(idx)
                else:
                    hash_table[nums[idx]] = [idx]
            else:
                for x in hash_table[(target - nums[idx])]:
                    item = [nums[x], nums[idx]]
                    if(item not in result):
                        result.append(item)
        return result


if __name__ == '__main__':
    solution = Solution()

    input = [1, 0, -1, 0, -2, 2]
    target = 0
    ans = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    res = solution.fourSum(input, target)
    print(f'input: {input}, target: {target}\nres: {res}\nans: {ans}\n')

    input = [-2, -1, -1, 1, 1, 2, 2]
    target = 0
    ans = [[-2, -1, 1, 2], [-1, -1, 1, 1]]
    res = solution.fourSum(input, target)
    print(f'input: {input}, target: {target}\nres: {res}\nans: {ans}\n')

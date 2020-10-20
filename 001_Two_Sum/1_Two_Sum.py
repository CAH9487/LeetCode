from typing import Any, List

'''
Runtime: 48 ms, faster than 80.32% of Python3 online submissions
Memory Usage: 15.4 MB, less than 16.25% of Python3 online submissions
'''
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
    if(len(nums) < 2):
      return []
    hash_table = {}
    for idx in range(len(nums)):
      if((target - nums[idx]) not in hash_table.keys()):
        hash_table[nums[idx]] = idx
      else:
        return [idx, hash_table[target - nums[idx]]]
            
if __name__ == '__main__':
  sln = Solution()
  print(sln.twoSum([2,7,11,15], 9))
  
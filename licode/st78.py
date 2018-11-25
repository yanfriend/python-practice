"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        don't use replace(difficult to filter out duplicates), always use loop!!!
        """
        ret=[]
        self.dfs(nums, 0, ret, [])
        return ret

    def dfs(self,nums, ind, ret, path):
        ret.append(path)
        for i in range(ind, len(nums)):
            self.dfs(nums, i+1,ret, path+[nums[i]])

print Solution().subsets([1,2,3])

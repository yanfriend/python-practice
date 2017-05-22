"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
import copy


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        nums.sort()
        visited=[False]*len(nums)
        self.dfs(nums,visited,ret,[])
        return ret

    def dfs(self, nums, visited, ret, per):
        if len(per) == len(nums):
            ret.append(per)
            return

        for i in range(len(nums)):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]: continue
            visited[i] = True
            self.dfs(nums, visited, ret, per + [nums[i]])
            visited[i] = False

print Solution().permuteUnique([1,1,2])

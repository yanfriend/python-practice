import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        self.dfs(nums,ret,0)
        return ret

    def dfs(self, nums, ret, ind):
        if ind==len(nums):
            ret.append(nums)
            return
        for i in range(ind,len(nums)):
            nums[i],nums[ind]=nums[ind],nums[i]
            self.dfs(copy.deepcopy(nums),ret,ind+1) # for this one, no copy and swap back is ok, but not for below one.
            # self.dfs(nums,ret,ind+1)
            # nums[i],nums[ind]=nums[ind],nums[i]

class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        nums.sort()
        self.perm(ret,nums,0)
        return ret

    def perm(self,ret, nums, ind):
        if ind==len(nums)-1:
            ret.append(nums)
            return
        for i in range(ind,len(nums)):
            if i!=ind and (nums[i]==nums[ind]): continue

            nums[ind],nums[i]=nums[i],nums[ind]
            self.perm(ret, copy.deepcopy(nums), ind+1)

print Solution().permute([1,2,3])
print Solution2().permuteUnique([1,1,2])

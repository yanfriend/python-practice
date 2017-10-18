import copy


class Solution(object):
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
            self.perm(ret, copy.deepcopy(nums), ind+1) # python, and c++ vector are diff.

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
            ret.append(copy.deepcopy(nums))
            return
        for i in range(ind,len(nums)):
            if i!=ind and (nums[i]==nums[ind]): continue

            nums[ind],nums[i]=nums[i],nums[ind]
            self.perm(ret, nums, ind+1) # python, and c++ vector are diff.
            nums[ind],nums[i]=nums[i],nums[ind]

l1=[1,1,2]
l2=[1,1,2,2]
l3=[1,2,2,3]
# print Solution().permuteUnique(l2)
# print Solution2().permuteUnique(l2) # not work

print Solution().permuteUnique(l3)
print Solution2().permuteUnique(l3) # not work

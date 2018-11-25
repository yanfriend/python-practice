class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                import ipdb;ipdb.set_trace()
                # tmp=nums[i]
                # nums[i]=nums[tmp-1]
                # nums[tmp-1]=tmp
                tmp=nums[i]
                nums[i],nums[tmp-1]=nums[tmp-1],nums[i]
        for i in range(len(nums)):
            if i!=nums[i]-1:
                return [nums[i],i+1]

print Solution().findErrorNums([3,2,2])

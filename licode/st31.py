class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # make it larger, but the smallest larger.
        found=False
        i=0 # remove to try ?
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                found=True
                break
        if not found: nums.sort(); return

        # i-1 is the key
        # min_val, ind=min([(val,ind) for ind,val in enumerate(nums[i:],i) if val>nums[i-1]])

        # instead of min, get the right most. same thing
        import ipdb;ipdb.set_trace()

        ind=len(nums)-1
        while ind<i-1 and nums[ind]<nums[i-1]: ind-=1

        nums[i-1],nums[ind]=nums[ind],nums[i-1]
        nums[i:]=reversed(nums[i:])


print Solution().nextPermutation([2,3,1])

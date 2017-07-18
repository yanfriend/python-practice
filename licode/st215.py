class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return None
        return self.range_find(nums,0,len(nums)-1,len(nums)-k) # change to ascending order, and to array index

    def range_find(self,nums,start,end,k):
        import ipdb;ipdb.set_trace()

        if start==end: return nums[k]

        pivot=nums[end]
        l=start; r=end-1
        while l<=r: # a better way to switch of just one loop
            if nums[l]<pivot: l+=1; continue
            if nums[r]>pivot: r-=1; continue
            nums[l],nums[r]=nums[r],nums[l]
            l+=1; r-=1
        nums[end],nums[l]=nums[l],nums[end]

        if l==k: return nums[l]
        elif l<k: return self.range_find(nums,l,end,k-l)
        else: return self.range_find(nums,start,l-1,k)

print Solution().findKthLargest([-1,-1],2)

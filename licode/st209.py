class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        ret=float('inf')
        l=0
        sum_so_far=0
        for r in range(len(nums)):
            sum_so_far+=nums[r]

            import ipdb;ipdb.set_trace()

            if sum_so_far>s:
                while sum_so_far>s and l<=r:
                    sum_so_far-=nums[l]
                    l+=1
            if sum_so_far==s:
                ret=min(ret,r-l+1)
        return ret

print Solution().minSubArrayLen(11,[1,2,3,4,5])

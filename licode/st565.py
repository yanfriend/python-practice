class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        visited=set()

        for i,n in enumerate(nums):
            self.traverse(nums, dp, i, visited)

        return max(dp)

    def traverse(self, nums, dp, ind, visited):
        if dp[ind] > 0: return dp[ind]

        org=ind
        cnt=1
        while nums[ind]!=org:
            dp[ind]=cnt
            cnt+=1
            ind=nums[ind]

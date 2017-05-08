class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)/2==1: return False
        all_sum=sum(nums)/2



        dp=[[False for j in range(0,all_sum+1)] for i in range(0,len(nums)+1)]
        import ipdb; ipdb.set_trace()
        for i in range(0,len(nums)+1):
            dp[i][0]=True

        # dp[i][j]=True if dp[i-1][j] is True; or dp[i-1][j-num[i]] is true
        for i in range(1,len(nums)+1):
            for j in range(1, all_sum+1):
                if j-nums[i-1]>=0:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:dp[i][j]=dp[i-1][j]

        self.pp(dp)

        return dp[len(nums)][all_sum]

    def pp(self,dp):
        for i in range(0,len(dp)):
            for j in range(0,len(dp[0])):
                print '{} '.format(dp[i][j]),
            print '\n'

print Solution().canPartition([1,2,3,5])


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret=0
        dp=[0]*(target+1)
        dp[0]=1

        for i in range(1,target+1):
            for j in range(len(nums)):
                if nums[j]<=i:
                    dp[i]+=dp[i-nums[j]]

        return dp[-1]

print Solution().combinationSum4([1,2,3],4)

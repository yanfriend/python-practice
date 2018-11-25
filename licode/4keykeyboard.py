class Solution(object):
    def maxA_brute(self, N): # brute force.
        ret=N
        for i in range(1,N-2): # why N-2? when i to N-3, you need three ctrl-a, c, v to N
            ret=max(ret,self.maxA(i)*(N-i-1)) # # all N-i remaining, 1 for select, 1 for copy,
            # remaining N-i-2 for past, + org one
        return ret

    def maxA(self, N):
        dp=[0]*(N+1)

        for i in range(1,N+1):
            dp[i]=i
            for j in range(1,i-2):
                dp[i]=max(dp[i],dp[j]*(i-j-1)) # 1 for select, 1 for copy (waste 2) + org one
        return dp[-1]

print Solution().maxA(3)
print Solution().maxA(7)

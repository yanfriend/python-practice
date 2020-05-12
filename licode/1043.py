class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0] * (len(A)+1)
        for i in range(len(A)):
            curr_max = 0
            for j in range(K):
                if i - j < 0: break
                curr_max = max(curr_max, A[i - j])
                dp[i+1] = max(dp[i+1], curr_max * (j + 1) + dp[i - j])
            print(dp)

        return dp[-1]

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10],3))

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0] * (K + W + 2)
        S = 0
        for k in range(N + W + 1, -1, -1):
            if k > N: continue
            if k >= K:
                dp[k] = 1
            else:
                dp[k] = S * 1.0 / W
            S = S + dp[k] - (0 if k + W > K + W else dp[k + W])
        return dp[0]

print Solution().new21Game(10,1,10)

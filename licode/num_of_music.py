class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        dp = [[0] * (N+1) for i in range(L+1)]  # L listened , row; N different songs, col
        dp[0][0] = 1
        mod = 10 ** 9 + 7;

        for l in range(1, L+1):
            for n in range(1, N+1):
                dp[l][n] = dp[l - 1][n - 1] * (N - n + 1)
                if n > K:
                    dp[l][n] = dp[l][n] + dp[l - 1][n] * (n - K)
        return dp[L][N] % mod

print Solution().numMusicPlaylists(3,3,1)

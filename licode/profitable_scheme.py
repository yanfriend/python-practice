import copy


class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 1000000007

        K = len(group)
        dp = [[[0] * (G + 1) for _ in range(P + 1)] for _ in range(K+1)]
        # dp = [copy.deepcopy(curr) for _ in range(K + 1)]
        dp[0][0][0] = 1

        for k in range(1, K + 1):
            p = profit[k - 1];
            g = group[k - 1]
            for i in range(P + 1):
                for j in range(G + 1):
                    dp[k][i][j] = (dp[k - 1][i][j] + (dp[k - 1][max(0, i - p)][j - g] if j >= g else 0)) % MOD
        return sum(dp[K][P]) % MOD


print Solution().profitableSchemes(5, 3, [2,2], [2,3])

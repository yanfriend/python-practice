class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = {i: 1 for i in A}
        A=sorted(A)
        for i, val in enumerate(A):
            for j in range(i):
                if val % A[j] == 0 and val / A[j] in dp:
                    dp[val] += dp[val / A[j]] * dp[A[j]]
                    dp[val] %= MOD
        return sum([val for val in dp.values()]) % MOD

print Solution().numFactoredBinaryTrees([18,3,6,2])

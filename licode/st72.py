class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)

        if not m or not n: return m or n

        dp=[[float('inf')]*(m+1) for _ in range(n+1)]
        for j in range(m): dp[0][j]=j
        for i in range(n): dp[i][0]=i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j]= min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) # dp[i][j]=dp[i-1][j-1] #
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[n][m]

print Solution().minDistance('olog', 'og')

def minDistance(word1, word2):
    m=len(word1); n=len(word2)
    dp=[[float('inf')]*(n+1) for _ in range(m+1)]

    # dp[0][0]=0

    for j in range(n+1): dp[0][j]=j # init
    for i in range(m+1): dp[i][0]=i

    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=min(dp[i][j],i+j)
            if word1[i-1]==word2[j-1]:
                dp[i][j]=min(dp[i][j],dp[i-1][j-1])
            else: # not equal
                dp[i][j]=min(dp[i][j],dp[i][j-1],dp[i-1][j])+1 # 1, miss dp[i-1][j-1] # replace

    return dp[m][n]

print minDistance('ab','a')
print minDistance('abcdef','abdf')

# below is mine in leetcode
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)

        dp=[[float('inf')]*(m+1) for _ in range(n+1)]
        for j in range(m+1): dp[0][j]=j
        for i in range(n+1): dp[i][0]=i

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1]==word2[i-1]:
                    dp[i][j]=dp[i-1][j-1] # min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) # wrong
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
        return dp[n][m]
